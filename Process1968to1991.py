'''
Created on 3 Dec 2018

@author: ostlerr
'''
import os
from YieldBookToData import *
import string
import configparser
import xmltodict
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
        return "-".join([str(self.sday),str(self.smonth),str(self.syear)])
    
    def endDate(self):
        if self.eday != "":
            if self.emonth == "":
                self.emonth = self.smonth
            if self.eyear == "":
                self.eyear = self.syear 
            return "-".join([self.eday,self.emonth,self.eyear])
        else:
            return ""

def looksLikeDay(word):
    nword = removePunctuation(word,["&","%","}"])
    if (len(nword) == 2 or len(nword) == 1):
        if nword in (["1b"]): # common errors which should be ignored
            return False
        numCount = 0
        for c in nword:
            if c.isdigit():
                numCount += 1
        if numCount >= 1:
            return True
    return False

def setYear(tyear):
    global lyear
    if tyear:
        tyear = removePunctuation(tyear,["&","%","}"])
        lyear = tyear
    elif lyear == "":
        lyear = year    

# this method is all about finding the end of a cultivations segment. If no end is found by the end of the page then carries through to the next page    
def getOperations(content):
    lines = content.split("\n")
    cultivationsSegment = []
    inCultivations = False
    for line in lines:
        if(inCultivations):
            if isStop(line):    
                inCultivations = False
                break
            else:                
                cultivationsSegment.append(line)
        elif startCultivations(line):
            cultivationsSegment.clear()
            inCultivations = True
            parts = line.split(" ")
            if (len(parts) >2):
                line = " ".join(parts[2:]) # why the start at index 2?
                cultivationsSegment.append(line)
    
    processCultivations(cultivationsSegment)

def writeJob(sname,opDates,curOp,prevOp):
    if not curOp:   
        curOp = prevOp
    curOp = curOp.strip()
    if curOp:
        if len(opDates) > 0:
            if opDates[0] == "variety":
                cleanCurOp = curOp.replace("variety:","").strip()
                outfile.write("|".join([str(experiment),str(year),str(sname).strip(),"","","variety",cleanCurOp]))
                outfile.write("\n")
            else:
                for opDate in opDates:
                    outfile.write("|".join([str(experiment),str(year),str(sname).strip(),opDate.startDate(),opDate.endDate(),"diary record",curOp]))
                    outfile.write("\n") 
    else:
        outfile.write("|".join([str(experiment),str(year),str(sname).strip(),"","","",curOp]))
        outfile.write("\n")
    return True

def applyCorrections(content):
    # Note this preserves lines as they provide structural cues to help with processing
    # some special force replacements - these could be applied to the whole doc
    
    content = re.sub(" +"," ",content).strip()
    content = content.replace("LO gals","40 gals")
    content = content.replace("=","-")
    content = content.replace("—","-")
    content = content.replace("~","-")
    content = content.replace("--","-")
    content = re.sub(r"My ([\d]{1,2})",r"May \1",content)
    content = re.sub(r"((?=[^23])\w),((?=[^46])\w)",r"\1, \2",content) # should ignore 2,4 3,6
    #content = re.sub(r" ([\d]{1,2}) and ",r" \1, ",content) # for fixing date formats 
    content = re.sub(r'((?=[^64pgnsbo])\w)-((?=[^dDtsmpC])\w)',r'\1 - \2',content) # ensures dashes are surrounded by spaces should ignore a few combinations... 3,6-dichlor.. Nitro-Chalk, 4-D, sub-plots, spring-tine, deep-tine, demeton-s-methyl
    
    return correctWords(content)

#this method is about subsectioning the cultivations then writing them             
def processCultivations(cultivationsSegment):   #cultivationSections = cultivationsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    # The text is formatted as a single block of text with no line breaks
    sectionName = ""
    subsections = {}
    subsectionText = ""
    print(cultivationsSegment)
    for idx, line in enumerate(cultivationsSegment):
        newSection, newLine = startsWithSection(line,sectionNames) 
        
        if newSection:
            if sectionName: # add the old section name to the dictionary. Length check is for misidentifications - sub sections should be short
                subsections[sectionName] = subsectionText
            subsectionText = "" #set up the new section text
            sectionName = newSection
            line = newLine
        elif idx == 0 and not sectionName: # for blank starting sections
            sectionName = "Not stated"
        #print(sectionName + " : " + newLine)
        
        if len(line) > 1:
            line = line.strip()
            if subsectionText[-1:] == "-":
                subsectionText = "".join([str(subsectionText),line])    
            else: 
                subsectionText = " ".join([str(subsectionText),line])
    if not sectionName:
        sectionName = "All plots"
    subsections[sectionName] = subsectionText           # got a new section...probably
    
    # Now process the subsections:
    processSections(subsections)

def stripLastPunctuation(word):
    chars = list(word.strip())
    punc = ""
    word = ""
    if chars[len(chars)-1] in (".",",",";",":"):
        word = "".join(chars[:-1])
        punc = chars[len(chars)-1]
    else: 
        word =  "".join(chars)
    return word, punc

def processSections(subsections):
    global lyear
    written = True
    for sname, stext in subsections.items():
        print(">>>>>>>>>>")
        print(sname)
        print(">>>>>>>>>>")
        print(stext)
        rawwords = applyCorrections(stext).split(" ")
        
        words = list(filter(filterPunctuation,rawwords)) #removes stray punctuation marks 
        lyear = ""
        curDates = []
        expectDay = False
        expectMonth = False
        expectDayOrMonth = False
        testYear = False
        expectEndDate = False
        prevOp = ""
        curOp = ""
        punc = ""
        for idx, tword in enumerate(words):
            written = False
            word, punc = stripLastPunctuation(tword)
            if word == "variety":
                print("12: " + word)
                curDates = checkCurDateYears(curDates)
                written = writeJob(sname,curDates,curOp, prevOp)
                curDates = ["variety"]
                curOp = ""
                expectDay = False
                testYear = False
            elif testYear:
                setYear("") # this forces a year if the first record has no year in the date
                if looksLikeDay(word):
                    print("0 " + word)
                    newDate = ObsDate()
                    newDate.sday = word
                    curDates.append(newDate)
                    print(newDate.startDate())
                    expectMonth = True
                    testYear = False
                elif word == "and":
                    print("1 " + word)
                    expectDay = True
                    testYear = False
                elif word in ("-","—","="):
                    print("2 " + word)
                    testYear = False
                    expectDayOrMonth = True
                    expectEndDate = True
                elif looksLikeYear(word):
                    print("3 " + word)
                    setYear(word)
                    for jdx in range(len(curDates)):
                        curDate = curDates[jdx]
                        curDate.syear = lyear
                        curDate.eyear = lyear
                        curDates[jdx] = curDate
                    written = writeJob(sname,curDates,curOp, prevOp)
                    testYear = False
                    expectDay = False
                    expectEndDate = False
                    prevOp = curOp if curOp else prevOp
                    curDates = []
                    curOp = ""
                elif word in months: # same operation, different date
                    print("4 " + word)
                    expectDay = False#True
                    testYear = True#False
                    curDate = ObsDate()
                    curDate.smonth = word
                    curDates.append(curDate)
                else: # new operation
                    print("5 " + word)
                    #no year has been set - get the year
                    for jdx in range(len(curDates)):
                        curDate = curDates[jdx]
                        curDate.syear = lyear
                        curDate.eyear = lyear
                        curDates[jdx] = curDate
                    written = writeJob(sname,curDates,curOp, prevOp)
                    curDates = []
                    prevOp = curOp if curOp else prevOp
                    curOp = word + punc
                    expectDay = False
                    testYear = False
            elif expectDayOrMonth:# this case is for after a dash
                if word in ("-","—","="):
                    print("6.2 " + word)
                    testYear = False
                    expectDayOrMonth = True
                    expectEndDate = True
                elif word in months:
                    testYear = True
                    print("7 " + word)
                    curDate = curDates.pop()
                    if expectEndDate:
                        curDate.emonth = word
                        if not curDate.smonth:
                            curDate.smonth = word
                    else:
                        curDate.smonth = word
                    curDates.append(curDate)
                    expectDayOrMonth = False
                else: 
                    print("8 " + word)
                    expectMonth = True
                    testYear = False
                    curDate = ""
                    if expectEndDate: # updating an existing date range
                        curDate = curDates.pop()
                        curDate.eday = word.replace(".","")
                    else: # new date
                        curDate = ObsDate()
                        curDate.sday = word.replace(".","")
                    curDates.append(curDate)
                    expectDay = False
                    expectDayOrMonth = False
            elif expectMonth:
                print("9 " + word)
                for jdx in range(len(curDates)):
                    tmonth = word.replace(".","").replace(",","")
                    curDate = curDates[jdx]
                    if expectEndDate:
                        curDate.emonth = tmonth
                        if curDate.smonth == "":
                            curDate.smonth = tmonth
                        expectEndDate = False
                    else:
                        if curDate.smonth == "":
                            curDate.smonth = tmonth
                    curDates[jdx] = curDate
                testYear = True
                expectMonth = False
            elif looksLikeDay(word) and idx+1 < len(words) and (words[idx+1] in ("-","=","~") or stripLastPunctuation(words[idx+1])[0] in months or looksLikeDay(stripLastPunctuation(words[idx+1])[0])):
                print("10 " + word)
                expectDayOrMonth = True
                testYear = False
                curDate = ObsDate()
                curDate.sday = word
                curDates.append(curDate)
            else:
                print("11 " + word)
                expectDay = False
                testYear = False
                word = word + punc
                curOp = " ".join([curOp,word])
                            
        if curDates and curDates[0] == "variety":
            print("POINT13 " + word)
            written = writeJob(sname,curDates,curOp, prevOp)
            curDates = []
            curOp = ""
        if not written:
            curDates = checkCurDateYears(curDates)
            writeJob(sname,curDates,curOp, prevOp)
            curOp = ""  

def checkCurDateYears(tCurDates):
    #global lyear
    for jdx in range(len(tCurDates)): # Probably won't have the year included
        tCurDate = tCurDates[jdx]
        #setYear(tCurDate.smonth,tCurDate.syear)
        if tCurDate.syear == "" or tCurDate == None:
            tCurDate.syear = lyear
            tCurDate.eyear = lyear
            tCurDates[jdx] = tCurDate
            print(tCurDate.startDate())
    return tCurDates
     
config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['ob_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
strSections = config['EXPERIMENT']['sections']
sectionNames = strSections.split(",")
print(sectionNames)
print("starting " + experiment)

lyear = ""
year = ""
with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    year = rep["year"]    
    if int(year) >=1968 and int(year) <= 1991:
        print("start processing year: " + str(year))
        content = rep["rawcontent"]
        content = removeBlankLines(content)
        getOperations(content)
        
        
outfile.close()        