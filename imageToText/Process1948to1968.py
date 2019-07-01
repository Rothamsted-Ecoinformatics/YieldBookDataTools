'''
Created on 3 Dec 2018

@author: ostlerr
'''
import os
from imageToText.YieldBookToData import *
import configparser

def cleanDate(dirtyDate, year):
    dirtyDate = removePunctuation(str(dirtyDate), ("-"))
    sDate = ""
    eDate = ""
    lyear = year # the local year from the date, rather than the doc
    dates = dirtyDate.split("-")
    if len(dates) > 0: # just one date
        sparts = dates[0].strip().split(" ")
        mnth = ""
        if len(sparts) == 2:
            sDate, mnth = formatDate(sparts[1],sparts[0],lyear)
        elif len(sparts) == 3:
            lyear = sparts[2]
            sDate, mnth = formatDate(sparts[1],sparts[0],lyear)            
        else:
            sDate = dirtyDate
        if len(dates) == 2:    
            eparts = dates[1].strip().split(" ")
            if len(eparts) == 1:
                eDate,month = formatDate(eparts[0],mnth,lyear)
            elif eparts[0] in months:
                eDate,month = formatDate(eparts[1],eparts[0],lyear)
            else:
                eDate,month = formatDate(eparts[0],mnth,lyear)
    return sDate,eDate
  
# this method is all about finding the end of a cultivations segment. If no end is found by the end of the page then carries through to the next page    
def getOperations(lines):
    global cultivationsSegment
    global inCultivations 
    print("----++++" + year)
    for line in lines:
        if(inCultivations):
            if isStop(line): 
                inCultivations = False
                print("ex cultivations")
            else:
                cultivationsSegment.append(line)
        elif fuzz.token_set_ratio(line,"Cultivations, etc.:") >= 75 or year == "1938": 
            print("++++" + year)
            cultivationsSegment.clear()
            inCultivations = True 
            print("in cultivations")
            parts = line.split(" ")
            if (len(parts) >2):
                line = " ".join(parts[2:])
                cultivationsSegment.append(line)
    processCultivations()
    
def writeJob(sname,opDate,curOp,prevOp):
    if not curOp:   
        curOp = prevOp
    if curOp:
        cleanCurOp = tidyOp(curOp)
        sDate, eDate = cleanDate(opDate,year)
        outfile.write("|".join([str(experiment),str(year),str(sname),str(sDate),str(eDate),cleanCurOp]))
        outfile.write("\n")    
    
    
def tidyOp(line): # Trims leading and trailing punctuation
    nline = line.strip()
    
    if (nline and nline[len(nline)-1] in [",",":","."]):
        nline = nline[0:len(nline)-1]
    
    if (nline and nline[0] in [",",":","."]):
        nline = nline[1:]
    
    nline = nline.strip() 
    return nline

def startsWithBlock(line):
    lline = line.lower()
    if (fuzz.token_set_ratio(lline,"block") >= 75):
        blockParts = line.split(" ",2)
        block = " ".join([blockParts[0],blockParts[1]])
        line = blockParts[2]
        return block, line
    else:
        return None,None        
        
#this method is about subsectioning the cultivations then writing them             
def processCultivations():   #cultivationSections = cultivationxsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    sectionName = ""
    blockName = ""
    subsections = {}
    subsectionText = ""
    for idx, line in enumerate(cultivationsSegment):
        line = line.replace(" and ",", ")
        newBlock, newLine = startsWithBlock(line)
        
        if newBlock:
            blockName = newBlock
            line = newLine.strip()
        newSection = None
        newLine = None
        
        if (line):
            newSection, newLine = startsWithSection(line,sectionNames) 

        if newSection or idx == 0: # Need the zero check in case of no section or dodgy section
            if sectionName: # add the old section name to the dictionary. 
                subsections[sectionName] = subsectionText
            subsectionText = "" #set up the new section text
            sectionName = " ".join([blockName,str(newSection)])
            line = newLine
        
        if (len(line) > 1):
            subsectionText = " ".join([str(subsectionText),line])
            
    if not sectionName:
        sectionName = "All plots"
    subsections[sectionName] = subsectionText           # got a new section...probably
    
    processSections(subsections)
        
def processSections(subsections):
    for sname, stext in subsections.items():
        print("===========")
        print(sname)
        print(stext)
        print("===========")
        curDate = None
        expectDay = False
        expectDayOrMonth = False
        testYear = False
        prevOp = ""
        curOp = ""
        words = stext.split(" ")
        for word in words:
            word = word.strip()
            if testYear:
                if (word == "-" or word == "="):
                    curDate = " ".join([str(curDate),str("-")])
                    testYear = False
                    expectDayOrMonth = True
                elif looksLikeYear(word):
                    curDate = " ".join([str(curDate),str(word)])
                    writeJob(sname,curDate,curOp, prevOp)
                    testYear = False
                    expectDay = False
                    prevOp = curOp if curOp else prevOp
                    curOp = ""
                elif word in months: # same operation, different date
                    writeJob(sname,curDate,curOp, prevOp)
                    expectDay = True
                    testYear = False
                    prevOp = curOp if curOp else prevOp
                    curDate = word
                else: # new operation
                    writeJob(sname,curDate,curOp, prevOp)
                    curDate = None
                    prevOp = curOp if curOp else prevOp
                    curOp = word 
                    expectDay = False
                    testYear = False
            elif expectDayOrMonth:# this case is for after a dash
                if word in months:
                    expectDay = True
                    curDate = " ".join([str(curDate),str(word)])
                else: 
                    curDate = " ".join([str(curDate),str(word).strip()])
                    testYear = True
                    expectDay = False
                expectDayOrMonth = False
            elif expectDay:
                curDate = " ".join([str(curDate),str(word).strip()])
                testYear = True
                expectDay = False
            elif word in months: # same operation, different date
                expectDay = True
                testYear = False
                curDate = word
            elif word == "variety":
                curDate = "variety"
            else:
                expectDay = False
                testYear = False
                curOp = " ".join([curOp,word])
        if curDate == "variety":
            writeJob(sname,curDate,curOp, prevOp)

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
strSections = config['EXPERIMENT']['sections']
sectionNames = strSections.split(",")
print(sectionNames)
cultivationsSegment = []
inCultivations = False
sectionStarts = ()
year = ""

fileList = os.listdir(srcdocs)
fileList.sort()

for idx, fname in enumerate(fileList):
    nyear = fname[0:4]
    if int(nyear) < 1968 and fname.endswith(".jpg"):
         
        print("processing document " + str(idx) + ", " +fname)
        inCultivations = True if (nyear == year) else False
        year = nyear
        page = getPageScan(srcdocs + "\\" + fname)
        page = re.sub(" +"," ",page).strip()
        lines = toCorrectedLines(page)        
        print(lines)
        getOperations(lines)
        
print('done')
outfile.close()