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
        return "-".join([self.sday,self.smonth,self.syear])
    
    def endDate(self):
        if self.eday != "":
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
    #print(opDate + " : " + curOp)
    if not curOp:   
        curOp = prevOp
    if curOp:
        #cleanCurOp = tidyOp(curOp)
        if len(opDates) > 0:
            if opDates[0] == "variety":
                cleanCurOp = curOp.replace("variety:","").strip()
                outfile.write("|".join([str(experiment),str(year),str(sname).strip(),"","","variety",cleanCurOp]))
                outfile.write("\n")
            #elif cleanCurOp.startswith("note:"):
            #    cleanCurOp = cleanCurOp.replace("note:","").strip()
            #    outfile.write("|".join([str(experiment),str(year),str(sname).strip(),"","","note",cleanCurOp]))
            #    outfile.write("\n")
            else:
                for opDate in opDates:
                    #sDate, eDate = cleanDate(opDate,year)
                    outfile.write("|".join([str(experiment),str(year),str(sname).strip(),opDate.startDate(),opDate.endDate(),"diary record",curOp]))
                    outfile.write("\n") 
    else:
        outfile.write("|".join([str(experiment),str(year),str(sname).strip(),"","","",curOp]))
        outfile.write("\n")
    return True

def writeJob_old(sname,opDate,op):
    sDate, eDate = cleanDate(opDate,year)
    outfile.write("|".join([str(experiment),str(year),str(sname),str(sDate),str(eDate),"diary record",op]))
    outfile.write("\n")    

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
    content = re.sub(r"((?=[^2])\w),((?=[^4])\w)",r"\1, \2",content) # should ignore 2,4
    content = re.sub(r" ([\d]{1,2}) and ",r" \1, ",content) # for fixing date formats 
    content = re.sub(r'((?=[^4pgnsbo])\w)-((?=[^DtsmpC])\w)',r'\1 - \2',content) # ensures dashes are surrounded by spaces should ignore a few combinations... Nitro-Chalk, 4-D, sub-plots, spring-tine, deep-tine, demeton-s-methyl
    
    return correctWords(content)
    #corrected = correctWords(content)
    #words = list(filter(None,corrected))
    #return " ".join(words)

#this method is about subsectioning the cultivations then writing them             
def processCultivations(cultivationsSegment):   #cultivationSections = cultivationsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    # The text is formatted as a single block of text with no line breaks
    sectionName = ""
    subsections = {}
    subsectionText = ""

    for line in cultivationsSegment:
        newSection, newLine = startsWithSection(line,sectionNames) 
        if (newSection):
            if(sectionName): # add the old section name to the dictionary. Length check is for misidentifications - sub sections should be short
                subsections[sectionName] = subsectionText
            subsectionText = "" #set up the new section text
            sectionName = newSection
            line = newLine
        
        if (len(line) > 1):
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

def processSections(subsections):
    global lyear
    written = True
    for sname, stext in subsections.items():
        print(stext)
        stext = stext.replace(".","").replace(",","")
        rawwords = applyCorrections(stext).split(" ")
        print(rawwords)
        
        words = list(filter(filterPunctuation,rawwords)) #removes stray punctuation marks 
        print(words)
        lyear = ""
        curDates = []
        expectMonth = False
        expectDayOrMonth = False
        testYear = False
        expectEndDate = False
        prevOp = ""
        curOp = ""
        
        for idx, word in enumerate(words):
            written = False
            word = word.strip().replace(",","")
            print(word)
            if testYear:
                if looksLikeDay(word):
                    print("0")
                    newDate = ObsDate()
                    newDate.sday = word
                    curDates.append(newDate)
                    print(newDate.startDate())
                    expectMonth = True
                    testYear = False
                elif word == "and":
                    print("1")
                    #for cd in curDates:
                    #    print("day: "  + cd.startDate())
                    #curDate = curDates[len(curDates)-1]
                    #newDate = ObsDate()
                    #newDate.smonth = curDate.smonth
                    #curDates.append(newDate)  
                    expectMonth = True
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
                    #expectDay = False
                    curDate = curDates.pop()
                    if expectEndDate:
                        curDate.emonth = word
                    else:
                        curDate.smonth = word
                    curDates.append(curDate)
                else: 
                    print("8")
                    expectMonth = True
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
            elif expectMonth:
                print("9")
                curDate = curDates.pop()
                curDate.smonth = word
                curDates.append(curDate)
                testYear = True
                expectMonth = False
            elif looksLikeDay(word) and (words[idx+1] in months or looksLikeDay(words[idx+1])):
                print(words[idx+1])
                print("10")
                expectMonth = True
                testYear = False
                curDate = ObsDate()
                curDate.sday = word
                curDates.append(curDate)
                 
            #elif word in months:
            #    print("10")
            #    expectDay = True
            #    testYear = False
            #    curDate = ObsDate()
            #    curDate.smonth = word
            #    curDates.append(curDate)
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

def processSections_old(subsections):
    for sname, stext in subsections.items():
        rawwords = applyCorrections(stext).split(" ")
        words = list(filter(filterPunctuation,rawwords)) #removes stray punctuation marks 
        wordCount = len(words)
        opDate = ""
        curOp = ""
        prevOp = ""
        opCount=0
        idx = 0
        backupOp = ""
        while idx < wordCount:
            word = words[idx]
            
            cleanWord = removePunctuation(word,["-","~", "="]) 
            trimCount = 0
            if cleanWord in months:                
                # check prev
                fd = words[idx-3]
                dash = words[idx-2]
                ld = words[idx-1]
                if looksLikeDay(ld):
                    if looksLikeDay(fd) and dash in ["-", "~","="]:
                        opDate = "-".join([fd,ld])
                        trimCount = 2 #? 
                    else:
                        opDate = ld
                        trimCount = 1
                    opDate = " ".join([opDate,cleanWord])
                    year = ""
                    base = 0
                    if idx+1 < wordCount and looksLikeYear(words[idx+1]):
                        year = removePunctuation(words[idx+1],[]) 
                        opDate = " ".join([opDate,year])
                        base = 1
                    
                    if idx+(3+base) < wordCount and words[idx+(1+base)] in ["-","~","="] and looksLikeDay(words[idx+2]) and removePunctuation(words[idx+(3+base)],[]) in months:
                        opDate = " ".join([opDate," - ", str(words[idx+(2+base)]), str(removePunctuation(words[idx+(3+base)],[]))])
                        base +=3
                    idx = idx+base
                    if opCount == 0:
                        flashCurOp = curOp.split(" ")
                        opPart = flashCurOp[:len(flashCurOp)-trimCount]
                        curOp = " ".join(opPart)
                        curOp = curOp.replace(":", "").strip()
                        if(len(curOp) <= 2):
                            curOp = backupOp
                        if curOp == "and":
                            curOp = backupOp
                        opCount = 1
                    writeJob(sname,opDate,curOp)
                    opDate = None
                else:
                    curOp = " ".join([curOp,word])
            elif opCount == 1 and looksLikeDay(cleanWord) or looksLikeYear(word) or word in ["-", "~", "="]:
                pass
            else:
                if opCount == 1:
                    backupOp = curOp
                    curOp = word
                else: 
                    curOp = " ".join([curOp,word])
                opCount = 0
                    
            idx+=1    
        if opDate:
            if curOp == "and":
                curOp = backupOp
            writeJob(sname,opDate,curOp,experiment)
     
def cleanDate(dirtyDate, year):
    global lyear
    sDate = ""
    eDate = ""

    if dirtyDate:
        dirtyDate = dirtyDate.replace("=","-").replace("—","-")
        dirtyDate = removePunctuation(str(dirtyDate), ("-"))
        dirtyDate = dirtyDate.replace(" and ",", ")
        dirtyDate = re.sub(r"(\d)-(\d)",r"\1 - \2",dirtyDate)

        parts = dirtyDate.split(" ")
        if re.match(r"\d{1,2} \w{3,5} - \d{1,2} \w{3,5} \d{4}",str(dirtyDate)):
            lyear = parts[5]
            sDate = "-".join([parts[0],parts[1],lyear])
            eDate = "-".join([parts[3],parts[4],lyear])
        elif re.match(r"\d{1,2} - \d{1,2} \w{3,5} \d{4}",str(dirtyDate)):
            lyear = parts[4]
            month = parts[3]
            sDate = "-".join([parts[0],month,lyear])
            eDate = "-".join([parts[2],month,lyear])
        elif re.match(r"\d{1,2} - \d{1,2} \w{3,5}",str(dirtyDate)):
            month = parts[3]
            sDate = "-".join([parts[0],month,lyear])
            eDate = "-".join([parts[2],month,lyear])
        elif re.match(r"\d{1,2} \w{3,5} \d{1,4}",str(dirtyDate)):
            lyear = parts[2]
            month = parts[1]
            sDate = "-".join([parts[0],month,lyear])        
        elif re.match(r"\d{1,2} \w{3,5}",str(dirtyDate)):
            if lyear == "":
                lyear = str(int(year)-1)
            month = parts[1]
            if (lyear == "" or lyear == str(int(year)-1)) and month in ("Jan","Feb","Mar","April","Apr","May","June","July"):
                lyear = year
            elif lyear == "":
                lyear = str(int(year)-1)

            sDate = "-".join([parts[0],month,lyear])
        else:
            sDate = "UNKNOWN"
            eDate = dirtyDate
            
    return sDate,eDate

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['ob_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
strSections = config['EXPERIMENT']['sections']
sectionNames = strSections.split(",")
print(sectionNames)
print("starting " + experiment)

year = ""
lyear = ""

with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    year = rep["year"]    
    if int(year) >=1968 and int(year) <= 1991:
        print("start processing year: " + str(year))
        content = rep["rawcontent"]
        content = removeBlankLines(content)
        getOperations(content)
        