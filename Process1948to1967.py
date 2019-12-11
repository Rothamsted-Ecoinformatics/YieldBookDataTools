'''
Created on 3 Dec 2018

@author: ostlerr
'''
import os
from YieldBookToData import removeBlankLines, startsWithSection, months, looksLikeYear, removePunctuation, isStop, filterPunctuation, correctWords, startCultivations
import configparser
import xmltodict
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import string
import re

def cleanDate(dirtyDate, year): # date format expects month first for this period
    global lyear
    sDate = ""
    eDate = ""
    if dirtyDate:
        dirtyDate = dirtyDate.replace("=","-").replace("—","-")
        dirtyDate = removePunctuation(str(dirtyDate), ("-"))
        dirtyDate = dirtyDate.replace(" and ",", ")
        print("dirtyDate: " + str(dirtyDate))

        parts = dirtyDate.split(" ")
        if re.match(r"\w{3,5} \d{1,2} - \w{3,5} \d{1,2} \d{4}",str(dirtyDate)):
            lyear = parts[5]
            sDate = "-".join([parts[1],parts[0],lyear])
            eDate = "-".join([parts[4],parts[3],lyear])
        elif re.match(r"\w{3,5} \d{1,2} - \d{1,2} \d{4}",str(dirtyDate)):
            lyear = parts[4]
            month = parts[0]
            sDate = "-".join([parts[1],month,lyear])
            eDate = "-".join([parts[3],month,lyear])
        elif re.match(r"\w{3,5} \d{1,2} - \d{1,2}",str(dirtyDate)):
            month = parts[0]
            sDate = "-".join([parts[1],month,lyear])
            eDate = "-".join([parts[3],month,lyear])
        elif re.match(r"\w{3,5} \d{1,2} \d{1,4}",str(dirtyDate)):
            lyear = parts[2]
            month = parts[0]
            sDate = "-".join([parts[1],month,lyear])        
        elif re.match(r"\w{3,5} \d{1,2}",str(dirtyDate)):
            if lyear == "":
                lyear = str(int(year)-1)
            month = parts[0]
            if (lyear == "" or lyear == str(int(year)-1)) and month in ("Jan","Feb","Mar","April","Apr","May","June","July"):
                lyear = year
            elif lyear == "":
                lyear = str(int(year)-1)

            sDate = "-".join([parts[1],month,lyear])
        else:
            sDate = "UNKNOWN"
            eDate = dirtyDate
            
    return sDate,eDate

def applyCorrections(content):
    # Note this preserves lines as they provide structural cues to help with processing
    # some special force replacements - these could be applied to the whole doc
    
    content = re.sub(" +"," ",content).strip()
    
    content = content.replace("LO gals","40 gals")
    content = content.replace("=","-")
    content = content.replace("—","-")
    content = content.replace("~","-")
    content = content.replace("--","-")
    content = re.sub(r'(\d{1,2}),',r'\1',content) # e.g. 1,
    content = re.sub(r'(\d{4});',r'\1,',content) # e.g. 1956;
    content = re.sub(r' [;.:] ',r' ',content)
    
    #content = re.sub(r"My ([\d]{1,2})",r"May \1",content)
    #content = re.sub(r"((?=[^2])\w),((?=[^4])\w)",r"\1, \2",content) # should ignore 2,4
    #content = re.sub(r" ([\d]{1,2}) and ",r" \1, ",content) # for fixing date formats 
    #content = re.sub(r'((?=[^4pgnsbo])\w)-((?=[^DtsmpC])\w)',r'\1 - \2',content) # ensures dashes are surrounded by spaces should ignore a few combinations... Nitro-Chalk, 4-D, sub-plots, spring-tine, deep-tine, demeton-s-methyl
    
    corrected = correctWords(content)
    words = list(filter(None,corrected))
    return " ".join(words)

# this method is all about finding the end of a cultivations segment. If no end is found by the end of the page then carries through to the next page    
def getOperations(content):
    print(content)
    print("IN OPERATIONS XXX")
    lines = content.split("\n")
    print(len(lines))
    inCultivations = False
    cultivationsSegment = []
    
    for line in lines:
        print("opline: " + line)
        if(inCultivations):
            if isStop(line): 
                inCultivations = False
                print("ex cultivations")
                break
            else:
                cultivationsSegment.append(line)
        elif startCultivations(line): #fuzz.token_set_ratio(line,"Cultivations, etc.:") >= 70: 
            inCultivations = True 
            print("in cultivations")
            
            parts = line.split(" ")
            if (len(parts) >2):
                line = " ".join(parts[2:])
                cultivationsSegment.append(line)
    processCultivations(cultivationsSegment)
    
def writeJob(sname,opDate,curOp,prevOp):
    if not curOp:   
        curOp = prevOp
    if curOp:
        cleanCurOp = tidyOp(curOp)
        vtype = ""
        if opDate == "variety":
            vtype = "variety"
            cleanCurOp = cleanCurOp.replace("variety:","").strip()
            opDate = ""
        elif cleanCurOp.startswith("note:"):
            vtype = "note"
            cleanCurOp = cleanCurOp.replace("note:","").strip()
        else:
            vtype = "diary record"
        sDate, eDate = cleanDate(opDate,year)
        outfile.write("|".join([str(experiment),str(year),str(sname),str(sDate),str(eDate),vtype,cleanCurOp]))
        outfile.write("\n") 
    return True   
    
    
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
def processCultivations(cultivationsSegment):   #cultivationSections = cultivationxsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    sectionName = ""
    blockName = ""
    subsections = {}
    subsectionText = ""
    for idx, line in enumerate(cultivationsSegment):
       
        #line = line.replace(" and ",", ")
        print(line)
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
    global lyear
    written = True
    for sname, stext in subsections.items():
        rawwords = applyCorrections(stext).split(" ")
        words = list(filter(filterPunctuation,rawwords)) #removes stray punctuation marks 
        
        lyear = ""
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
        for word in words:
            print(str(word) + " : " + str(testYear) + " : " + str(expectDay) + " : " + str(curDate))
            written = False
            word = word.strip()
            if testYear:
                if word in ("-","—","="):
                    curDate = " ".join([str(curDate),str("-")])
                    testYear = False
                    expectDayOrMonth = True
                elif looksLikeYear(word):
                    curDate = " ".join([str(curDate),str(word)])
                    written = writeJob(sname,curDate,curOp, prevOp)
                    testYear = False
                    expectDay = False
                    print("looks like year: " + curDate)
                    prevOp = curOp if curOp else prevOp
                    curOp = ""
                elif word in months: # same operation, different date
                    written = writeJob(sname,curDate,curOp, prevOp)
                    expectDay = True
                    testYear = False
                    prevOp = curOp if curOp else prevOp
                    curDate = word
                else: # new operation
                    written = writeJob(sname,curDate,curOp, prevOp)
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
            if word.startswith("variety"):
                curDate = "variety"
                curOp = ""
        if curDate == "variety":
            print("variety: " + curOp)
            written = writeJob(sname,curDate,curOp, prevOp)
            curDate = ""
            curOp = ""
    if not written:
        print("not written")
        writeJob(sname,curDate,curOp, prevOp)
        curOp = ""

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['oa_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
strSections = config['EXPERIMENT']['sections']
sectionNames = strSections.split(",")
print(sectionNames)
sectionStarts = ()
lyear = ""

with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    year = rep["year"]    
    if int(year) >=1948 and int(year) <= 1967:
        print("start processing year: " + str(year))
        content = rep["rawcontent"]
        content = removeBlankLines(content)
        getOperations(content)
print('done')
outfile.close()