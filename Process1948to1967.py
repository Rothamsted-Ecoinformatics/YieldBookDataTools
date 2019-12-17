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

class ObsDate():
    def __init__(self):
        self.sday = ""
        self.smonth = ""
        self.syear = ""
        self.eday = ""
        self.emonth = ""
        self.eyear = ""

    def startDate(self):
        return "-".join([self.sday,self.smonth,self.syear])
    
    def endDate(self):
        if self.eday != "":
            return "-".join([self.eday,self.emonth,self.eyear])
        else:
            return ""

def cleanDate(dirtyDate, year): # date format expects month first for this period
    global lyear
    sDate = ""
    eDate = ""
    print (dirtyDate)
    if dirtyDate:
        dirtyDate = dirtyDate.replace("=","-").replace("—","-")
        dirtyDate = removePunctuation(str(dirtyDate), ("-"))
        dirtyDate = dirtyDate.replace(" and ",", ")
        
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
    content = content.replace(" et "," at ")
    content = re.sub(r'(\d{1,2}),',r'\1',content) # e.g. 1,
    content = re.sub(r'(\d{4});',r'\1,',content) # e.g. 1956;
    content = re.sub(r' [;.:] ',r' ',content)

    return correctWords(content)

# this method is all about finding the end of a cultivations segment. If no end is found by the end of the page then carries through to the next page    
def getOperations(content):
    lines = content.split("\n")
    inCultivations = False
    cultivationsSegment = []
    
    for line in lines:
        if(inCultivations):
            if isStop(line): 
                inCultivations = False
                print("ex cultivations")
                break
            else:
                cultivationsSegment.append(line)
        elif startCultivations(line): #fuzz.token_set_ratio(line,"Cultivations, etc.:") >= 70: 
            inCultivations = True 
            parts = line.split(" ")
            if (len(parts) >2):
                line = " ".join(parts[2:])
                cultivationsSegment.append(line)
    processCultivations(cultivationsSegment)
    
def writeJob(sname,opDates,curOp,prevOp):
    #print(opDate + " : " + curOp)
    if not curOp:   
        curOp = prevOp
    if curOp:
        cleanCurOp = tidyOp(curOp)
        if len(opDates) == 1 and opDates[0] == "variety":
            cleanCurOp = cleanCurOp.replace("variety:","").strip()
            outfile.write("|".join([str(experiment),str(year),str(sname).strip(),"","","variety",cleanCurOp]))
            outfile.write("\n")
        elif cleanCurOp.startswith("note:"):
            cleanCurOp = cleanCurOp.replace("note:","").strip()
            outfile.write("|".join([str(experiment),str(year),str(sname).strip(),"","","note",cleanCurOp]))
            outfile.write("\n")
        else:
            for opDate in opDates:
                #sDate, eDate = cleanDate(opDate,year)
                outfile.write("|".join([str(experiment),str(year),str(sname).strip(),opDate.startDate(),opDate.endDate(),"diary record",cleanCurOp]))
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
        curDates = []
        expectDay = False
        expectDayOrMonth = False
        testYear = False
        expectEndDate = False
        prevOp = ""
        curOp = ""
        for word in words:
            written = False
            word = word.strip()
            print(word + " : " + str(curDates))
            if testYear:
                if word == "and":
                    print("1")
                    for cd in curDates:
                        print("day: "  + cd.startDate())
                    curDate = curDates[len(curDates)-1]
                    newDate = ObsDate()
                    newDate.smonth = curDate.smonth
                    curDates.append(newDate)  
                    expectDay = True
                    testYear = False
                    print("===========")
                    for cd in curDates:
                        print("day: "  + cd.startDate())
                elif word in ("-","—","="):
                    print("2")
                    #curDate = curDates[len(curDates)-1]
                    #curDate.sday = ""
                    #curDate.start = False
                    #curDates.append(curDate)
                    testYear = False
                    expectDayOrMonth = True
                    expectEndDate = True
                elif looksLikeYear(word):
                    print("3")
                    for jdx in range(len(curDates)):
                        curDate = curDates[jdx]
                        #if (lyear == "" or lyear == str(int(year)-1)) and curDate.smonth in ("Jan","Feb","Mar","April","Apr","May","June","July"):
                        #    lyear = year
                        print(curDate)
                        print("the word is: " + word)
                        curDate.syear = word.replace(".","")
                        curDate.eyear = word.replace(".","")
                        curDates[jdx] = curDate
                    written = writeJob(sname,curDates,curOp, prevOp)
                    testYear = False
                    expectDay = False
                    expectEndDate = False
                    prevOp = curOp if curOp else prevOp
                    curDates = []
                    curOp = ""
                elif word in months: # same operation, different date
                    print("4")
                    #written = writeJob(sname,curDates,curOp, prevOp)
                    expectDay = True
                    testYear = False
                    #prevOp = curOp if curOp else prevOp
                    curDate = ObsDate()
                    curDate.smonth = word
                    curDates.append(curDate)
                else: # new operation
                    print("5")
                    #no year has been set - get the year
                    for jdx in range(len(curDates)):
                        curDate = curDates[jdx]
                        if (lyear == "" or lyear == str(int(year)-1)) and curDate.smonth in ("Jan","Feb","Mar","April","Apr","May","June","July","Aug"):
                            lyear = year
                        elif lyear == "": 
                            lyear = str(int(year)-1)
                        curDate.syear = lyear
                        curDate.eyear = lyear
                        curDates[jdx] = curDate
                    written = writeJob(sname,curDates,curOp, prevOp)
                    curDates = []
                    prevOp = curOp if curOp else prevOp
                    curOp = word 
                    expectDay = False
                    testYear = False
            elif expectDayOrMonth:# this case is for after a dash
                print("6")
                if word in months:
                    print("7")
                    expectDay = True
                    curDate = curDates.pop()
                    if expectEndDate:
                        curDate.emonth = word
                    else:
                        curDate.smonth = word
                    curDates.append(curDate)
                else: 
                    print("8")
                    curDate = curDates.pop()
                    if expectEndDate:
                        curDate.eday = word.replace(".","")
                    else:
                        curDate.sday = word.replace(".","")
                    curDates.append(curDate)
                    testYear = True
                    expectDay = False
                    # look ahead to test for "and"
                    #if words[idx+1] == "and":
                    #    curDates.append(curDate)
                    #    idx += 1
                    #    expectDay = True
                    #    testYear = False
                expectDayOrMonth = False
            elif expectDay:
                print("9")
                curDate = curDates.pop()
                curDate.sday = word.replace(".","")
                curDates.append(curDate)
                testYear = True
                expectDay = False
            elif word in months:
                print("10")
                expectDay = True
                testYear = False
                curDate = ObsDate()
                curDate.smonth = word
                curDates.append(curDate)
            else:
                print("11")
                expectDay = False
                testYear = False
                curOp = " ".join([curOp,word])
            if word.startswith("variety"):
                print("12")
                curDates = ["variety"]
                curOp = ""
        if curDates and curDates[0] == "variety":
            print("13")
            written = writeJob(sname,curDates,curOp, prevOp)
            curDates = []
            curOp = ""
    if not written:
        writeJob(sname,curDates,curOp, prevOp)
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
        print(content)
        content = removeBlankLines(content)
        getOperations(content)
    
print('done')
outfile.close()