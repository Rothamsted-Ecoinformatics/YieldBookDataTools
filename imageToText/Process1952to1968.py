'''
Created on 3 Dec 2018

@author: ostlerr
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
import string

cultivationsSegment = []
code = ""
title = ""
hasMetadata = False
inCultivations = False
year = None
outfile = None
sectionStarts = ()
sectionNames = ()
experiment = None
corrections = []
    
with open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\corrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())

months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")

def globals(poutfile,psectionNames, psectionStarts,pexperiment):   
    global outfile
    global sectionNames
    global sectionStarts
    global experiment
    outfile = poutfile
    sectionNames = psectionNames
    sectionStarts = psectionStarts
    experiment = pexperiment
    
    print(sectionNames)

# Looks for any 4 character word and if it has at least 3 numbers assumes it is a number
def looksLikeYear(word):
    nword = removePunctuation(word,("&","%","}"))
    if (len(nword) == 4): 
        numCount= 0
        for c in nword:
            if c.isdigit():
                numCount += 1
        if numCount >= 3 or (numCount == 2 and nword[0:2] == "19"):
            return True
    return False 
      
def cleanDate(dirtyDate, year):
    dirtyDate = removePunctuation(str(dirtyDate), ("-"))
    sDate = ""
    eDate = ""
    
    dates = dirtyDate.split("-")
    if len(dates) == 1: # just one date
        parts = dates[0].strip().split(" ")
        if len(parts) == 2 or len(parts) == 3:
            sDate, month = formatDate(parts[1],parts[0],year)
        else:
            sDate = dirtyDate    
    elif len(dates) == 2:
        sparts = dates[0].strip().split(" ")
        mnth = ""
        if len(sparts) == 2 or len(sparts) == 3:
            sDate, mnth = formatDate(sparts[1],sparts[0],year)
        else:
            sDate = dirtyDate
        
        eparts = dates[1].strip().split(" ")
        if len(eparts) == 1:
            eDate,month = formatDate(eparts[0],mnth,year)
        else:
            if eparts[0] in months:
                eDate,month = formatDate(eparts[1],eparts[0],year)
            else:
                eDate,month = formatDate(eparts[0],mnth,year)
    return sDate,eDate
  
# this method is all about finding the end of a cultivations segment. If no end is found by the end of the page then carries through to the next page    
def getOperations(lines):
    global cultivationsSegment
    global inCultivations 
    for line in lines:
        print(line)
        if(fuzz.token_set_ratio(line,"Cultivations, etc.:") >= 75): 
            cultivationsSegment.clear()
            inCultivations = True
            parts = line.split(" ")
            if (len(parts) >2):
                line = " ".join(parts[2:])
                cultivationsSegment.append(line)
        elif(inCultivations):
            # Need to do something with notes    
            if(fuzz.ratio(line.lower(),"summary of Results") > 80 or fuzz.ratio(line.lower(),"standard errors") > 80):    
                processCultivations()
                inCultivations = False
                print("ex cultivations")
            else:
                cultivationsSegment.append(line)
    if (inCultivations):
        processCultivations()
    
def writeJob(sname,opDate,curOp,prevOp):
    global outfile
    global experiment
    global year
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

def startsWithSection(line):
    global sectionNames
    #lline = line.lower()
    #for name in sectionNames:
    #    if lline.startswith(name):
    #        return name, line[len(name):]
    #return None,None
    #print ("sectionNames: " + str(sectionNames))
    print(" line : "  + line)
    tline = removePunctuation(line,[]).strip()
    print(" tline : "  + tline)
    if tline and tline.find(" ") > -1:
        startParts = tline.split(" ",2)
        print("startParts: " + str(startParts))
        matchedStart = process.extractOne(str(startParts[0]),sectionStarts,scorer=fuzz.token_set_ratio,score_cutoff=65)
        print(str(matchedStart) + " :|: " + str(startParts[0]))
        if startParts[0] in sectionStarts or matchedStart:
            ok=True
            if (matchedStart[0] == "seed" or matchedStart[0] == "seed") and not process.extractOne(startParts[1],"hay",scorer=fuzz.token_set_ratio,score_cutoff=90):
                ok = False
            if ok:
                matched = process.extractOne(line,sectionNames,scorer=fuzz.token_set_ratio,score_cutoff=40)
                print("match: " + str(matched) + " |:| " + line)
                if matched:
                    print(matched[0] + " " +  str(len(matched[0])))
                    line = line[len(matched[0]):]
                    print (line)
                    return matched[0],line
    #        else: 
    #        return None,None
    #else:
    return None,None

def startsWithBlock(line):
    lline = line.lower()
    if (fuzz.token_set_ratio(lline,"block") >= 75):
        blockParts = line.split(" ",2)
        block = " ".join([blockParts[0],blockParts[1]])
        line = blockParts[2]
        return block, line
    else:
        return None,None        
    
def toCorrectedLines(page):
    print (page)
    lines = page.split("\n")
    cleanLines = []
    for line in lines:
        rawwords = line.split(" ") # chunk everything into words
        corrected = correctWords(rawwords,corrections)
        #print(corrected)
        cleanwords = corrected.split(" ")
        words = list(filter(None,cleanwords))
        #print("words: " + str(words))
        cleanLine = " ".join(words)
        #print("cleanLine: " + cleanLine)
        cleanLines.append(cleanLine)
    return cleanLines
        
#this method is about subsectioning the cultivations then writing them             
def processCultivations():   #cultivationSections = cultivationsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    #print("cultivation sections = " + str(len(cultivationSections)))
    sectionName = ""
    blockName = ""
    subsections = {}
    subsectionText = ""
    for line in cultivationsSegment:
        line = line.replace(" and ",", ")
        print(line)
        newBlock, newLine = startsWithBlock(line)
        print(newBlock)
        if newBlock:
            blockName = newBlock
            line = newLine.strip()
            print(" NEW BLOCK: " + blockName + " ||| " + newLine)
        newSection = None
        newLine = None
        if (line):
            newSection, newLine = startsWithSection(line) 
        
        print("newSection: " + str(newSection))
        if newSection:
            if sectionName: # add the old section name to the dictionary. Length check is for misidentifications - sub sections should be short
                subsections[sectionName] = subsectionText
            subsectionText = "" #set up the new section text
            print(" NEW SECTION: " + blockName + " " + newSection)
            sectionName = " ".join([blockName,newSection])
            line = newLine
        
        if (len(line) > 1):
            subsectionText = " ".join([str(subsectionText),line])
    if not sectionName:
        sectionName = "All plots"
    subsections[sectionName] = subsectionText           # got a new section...probably
    
    # Now process the subsections:
    print("WRITING JOBS:")
    processSections(subsections)
        
def processSections(subsections):
    for sname, stext in subsections.items():
        print(sname)
        print("=================")
        print (stext)
        #parts = stext.split(" ") # chunk everything into words
        
        curDate = None
        expectDay = False
        expectDayOrMonth = False
        testYear = False
        #corrected = correctWords(parts,corrections)
        #rawwords = corrected.split(" ")
        #words = list(filter(None,rawwords))
        prevOp = ""
        curOp = ""
        words = stext.split(" ")
        for word in words:
            word = word.strip()
            if testYear:
                #yearMatch = re.search("[0-9]{4}", word) 
                print(curDate)
                if (word == "-" or word == "="):
                    print ("dash up")
                    curDate = " ".join([str(curDate),str("-")])
                    testYear = False
                    expectDayOrMonth = True
                elif looksLikeYear(word):
                    #curDate = " ".join([str(curDate),str(yearMatch.group(0))])
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
            else:
                expectDay = False
                testYear = False
                curOp = " ".join([curOp,word])
        if curDate != "None":
            writeJob(sname,curDate,curOp, prevOp)

def loopDocs(dir):
    global year
    year = ""
    fileList = os.listdir(dir)
    fileList.sort()
    
    for idx, fname in enumerate(fileList):
        nyear = fname[0:4]
        if int(nyear) < 1968 and fname.endswith(".jpg"):
             
            print("processing document " + str(idx) + ", " +fname)
            
            inCultivations = True if (nyear == year) else False
            year = nyear
            page = getPageScan(dir + "\\" + fname)
            page = re.sub(" +"," ",page).strip()
            lines = toCorrectedLines(page)        
            getOperations(lines)
    outfile.close()

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
strSections = config['EXPERIMENT']['sections']
print(strSections)
sectionsNames = strSections.split(",")
loopDocs()
print('done')