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
            if self.emonth == "":
                self.emonth = self.smonth
            if self.eyear == "":
                self.eyear = self.syear 
            return "-".join([self.eday,self.emonth,self.eyear])
        else:
            return ""

def applyCorrections(content):
    # Note this preserves lines as they provide structural cues to help with processing
    # some special force replacements - these could be applied to the whole doc
    content = re.sub(" +"," ",content).strip()
    content = content.replace("LO gals","40 gals")
    content = content.replace("=","-")
    content = content.replace("—","-")
    content = content.replace("~","-")
    content = content.replace("--","-")
    ##content = content.replace(" and ", ", ")
    content = re.sub(r'([0-9])-([1-9])',r'\1 - \2',content)
    content = re.sub(r'([0-9])-([ADFJNOS])',r'\1 - \2',content)
    content = content.replace(" et "," at ")
    content = re.sub(r'(\d{1,2}),',r'\1',content) # e.g. 1,
    content = re.sub(r'(\d{4});',r'\1,',content) # e.g. 1956;
    content = re.sub(r' [;.:] ',r' ',content)

    return correctWords(content)
 
def writeJob(sname,opDates,curOp,prevOp):
    if not curOp:   
        curOp = prevOp
    if curOp:
        cleanCurOp = tidyOp(curOp)
        if cleanCurOp.startswith("note:"):
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

def setYear(tmonth, year):
    global lyear
    if (lyear == "" or lyear == str(int(year)-1)) and tmonth in ("Jan","Feb","Mar","April","Apr","May","June","July","Aug"):
        lyear = year
    elif lyear == "": 
        lyear = str(int(year)-1) 
    
#this method is about subsectioning the cultivations then writing them             
def processCultivations(content):   #cultivationSections = cultivationxsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    sectionName = ""
    subsections = {}
    subsectionText = ""
    lines = content.split("\n")
    for line in lines:
        if line.startswith("##"):
            if sectionName: # add the old section name to the dictionary. 
                subsections[sectionName] = subsectionText
            subsectionText = "" #set up the new section text
            sectionName = line.replace("##","")
        elif (len(line) > 1):
            subsectionText = " ".join([str(subsectionText),line])
            
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
        wasYear = False
        prevOp = ""
        curOp = ""
        for word in words:
            written = False
            word = word.strip()
            #print(word) 
            if testYear:
                if word == "and":
                    ##print("1: " + word)
                    curDate = curDates[len(curDates)-1]
                    newDate = ObsDate()
                    newDate.smonth = curDate.smonth
                    curDates.append(newDate)  
                    expectDayOrMonth = True
                    testYear = False
                elif word in ("-","—","="):
                    ##print("2: " + word)
                    testYear = False
                    expectDayOrMonth = True
                    expectEndDate = True
                elif looksLikeYear(word):
                    ##print("3: " + word)
                    wasYear = True
                    lyear = word.replace(".","").replace(",","").replace(":","")
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
                    ##print("4: " + word)
                    expectDay = True
                    testYear = False
                    # check year for the previous date
                    curDate = curDates.pop()
                    if (curDate):
                        setYear(curDate.smonth,year)
                        curDate.syear = lyear
                        curDates.append(curDate)
                    # start the new date
                    curDate = ObsDate()
                    curDate.smonth = word
                    curDates.append(curDate)                                    
                else: # new operation
                    ##print("5: " + word)
                    #no year has been set - get the year
                    for jdx in range(len(curDates)):
                        curDate = curDates[jdx]
                        setYear(curDate.smonth,year)
                        curDate.syear = lyear
                        curDate.eyear = lyear
                        curDates[jdx] = curDate
                    written = writeJob(sname,curDates,curOp, prevOp)
                    curDates = []
                    prevOp = curOp if curOp else prevOp
                    curOp = word 
                    expectDay = False
                    testYear = False
            ##elif word == "and": ## skip
            ##    pass
            elif expectDayOrMonth:# this case is for after a dash
                #print("6: " + word)
                
##                    expectDayOrMonth = True
                if word in months:
                    ##print("7: " + word)
                    expectDay = True
                    curDate = curDates.pop()
                    if expectEndDate:
                        curDate.emonth = word
                    else:
                        curDate.smonth = word
                    curDates.append(curDate)
                else: 
                    ##print("8: " + word + ", expectEndDate: " + str(expectEndDate))
                    curDate = curDates.pop()
                    if expectEndDate:
                        curDate.eday = word.replace(".","")
                        expectEndDate = False
                    else:
                        curDate.sday = word.replace(".","")
                    curDates.append(curDate)
                    testYear = True
                    expectDay = False
                expectDayOrMonth = False
            elif expectDay:
                ##print("9: " + word + ", expectEndDate: " + str(expectEndDate))
                curDate = curDates.pop()
                if expectEndDate:
                    curDate.eday = word.replace(".","")
                    expectEndDate = False
                else:
                    curDate.sday = word.replace(".","")
                curDates.append(curDate)
                testYear = True
                expectDay = False
                expectEndDate = False
            elif word in months:
                ##print("10: " + word)
                expectDay = True
                testYear = False
                curDate = ObsDate()
                curDate.smonth = word
                curDates.append(curDate)
            else:
                ##print("11: " + word)
                
                if wasYear and word == "and":
                    pass
                else: 
                    expectDay = False
                    testYear = False
                    curOp = " ".join([curOp,word])
                wasYear = False
        if not written:
            for jdx in range(len(curDates)):
                curDate = curDates[jdx]
                curDate.syear = lyear
                curDate.eyear = lyear
                curDates[jdx] = curDate
            
            #if curDates:
            #    curDate = curDates.pop()
            #    setYear(curDate.smonth,year)
            #    curDate.syear = lyear
            #    curDates.append(curDate)
            writeJob(sname,curDates,curOp, prevOp)
            curOp = ""
    ##if not written:
    ##    writeJob(sname,curDates,curOp, prevOp)
    ##    curOp = ""

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['oa_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
lyear = ""

with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    year = rep["year"]  
    if int(year) >=1938 and int(year) <= 1967:
        print("start processing year: " + str(year))
        content = rep["rawcontent"]
        ##print(content)
        content = removeBlankLines(content)
        processCultivations(content)
    
print('done')
outfile.close()