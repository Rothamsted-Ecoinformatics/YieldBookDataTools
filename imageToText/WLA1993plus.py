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
#expt = "Broadbalk"

# Looks for any 4 character word and if it has at least 3 numbers assumes it is a number
def looksLikeYear(word):
    
    nword = removePunctuation(word,["&","%","}"])
    if (len(nword) == 4): 
        numCount= 0
        for c in nword:
            if c.isdigit():
                numCount += 1
        if numCount >= 3 or (numCount == 2 and nword[0:2] == "19"):
            return True
    return False 
        
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
         
def removePunctuation(value, exclusions):
    result = ""
    for c in value:
        if c in exclusions or c not in string.punctuation:
            result += c
    return result
    
# this method is all about finding the end of a cultivations segment. If no end is found by the end of the page then carries through to the next page    
def getOperations(lines):
    global cultivationsSegment
    global inCultivations
    expt = "Broadbalk"    
    for line in lines:
        print(line)
        if (fuzz.token_set_ratio(line,"Broadbalk Wilderness") >= 75):
            
            processCultivations(expt)
            expt = "Broadbalk Wilderness"
            cultivationsSegment.clear()
            inCultivations = True
        
        elif(inCultivations):
            # Need to do something with notes    
            if(fuzz.ratio(line,"Summary of Results") > 80 or fuzz.ratio(line,"Standard errors") > 80):    
                processCultivations(expt)
                inCultivations = False
                print("ex cultivations")
            else:
                cultivationsSegment.append(line)
        elif(fuzz.token_set_ratio(line,"Cultivations etc") >= 75): 
            print("in cultivations")
            cultivationsSegment.clear()
            inCultivations = True
            parts = line.split(" ")
            if (len(parts) >2):
                line = " ".join(parts[2:])
                cultivationsSegment.append(line)
    if (inCultivations):
        processCultivations(expt)
    
def writeJob(sname,opDate,op,expt):
    ofOperations.write("|".join([expt,year,str(sname),opDate,op.strip()]))
    ofOperations.write("\n")    

def tidyOp(line): # Trims leading and trailing punctuation
    nline = line.strip()
    
    if (nline and nline[len(nline)-1] in [",",":","."]):
        nline = nline[0:len(nline)-1]
    
    if (nline and nline[0] in [",",":","."]):
        nline = nline[1:]
    
    nline = nline.strip() 
    return nline

def startsWithSection(line):
    sectionNames = ("crop sections","cropped sections", "all sections", "fallow sections", "fallow section", "potatoes", "spring beans", "winter wheat", "fallow", "w wheat", "w. wheat", "broadbalk wilderness", "grazed meadow", "ungrazed meadow", "woodland")
    lline = line.lower()
    for name in sectionNames:
        if lline.startswith(name):
            return name, line[len(name):]
    return None,None

def toCorrectedLines(page):
    lines = page.split("\n")
    lines = list(filter(None,lines))
    cleanLines = []
    for line in lines:
        rawwords = line.split(" ") # chunk everything into words
        corrected = correctWords(rawwords,corrections)
        cleanwords = corrected.split(" ")
        words = list(filter(None,cleanwords))
        cleanLine = " ".join(words)
        cleanLines.append(cleanLine)
    return cleanLines
        
#this method is about subsectioning the cultivations then writing them             
def processCultivations(experiment):   #cultivationSections = cultivationsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    #print("cultivation sections = " + str(len(cultivationSections)))
    sectionName = ""
    subsections = {}
    subsectionText = ""
    print ("processing for: " + experiment)
    for line in cultivationsSegment:
        line = line.replace(" and ",", ")
        
        newSection, newLine = startsWithSection(line) 
        if (newSection):
            if(sectionName): # add the old section name to the dictionary. Length check is for misidentifications - sub sections should be short
                subsections[sectionName] = subsectionText
            subsectionText = "" #set up the new section text
            sectionName = newSection
            line = newLine
        
        if (len(line) > 1):
            subsectionText = " ".join([str(subsectionText),line])
    if not sectionName:
        sectionName = "All plots"
    subsections[sectionName] = subsectionText           # got a new section...probably
    
    # Now process the subsections:
    processSections(experiment,subsections)

def filterPunctuation(rawword):
    if rawword in ["-","~"]:
        return True
    elif rawword in string.punctuation or rawword == " ":
        print("removed rawword: " + rawword)
        return False
    else:        
        return True
            
def processSections(experiment,subsections):
    for sname, stext in subsections.items():
        print("NEW SECTION:::" + sname)
        print(stext)
        print("END SECTION:::" + sname)
        
        
        rawwords = stext.split()
        words = list(filter(filterPunctuation,rawwords))
        wordCount = len(words)
        opDate = ""
        curOp = ""
        reset = False
        opCount=0
        idx = 0
        while idx < wordCount:
            word = words[idx]
            print("idx: " + str(idx) + " word: " + word + " (" + str(opCount) + ") : " + curOp)
            
        #for idx, word in enumerate(words):
            
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
                        #idx = idx+1 # skip the year
                        opDate = " ".join([opDate,year])
                        base = 1
                    print (str(base) + " " + year)
                    if idx+(3+base) < wordCount:
                        print (words[idx+(1+base)] + " " + words[idx+(2+base)] + " " + words[idx+(3+base)])
                    if idx+(3+base) < wordCount and words[idx+(1+base)] in ["-","~","="] and looksLikeDay(words[idx+2]) and removePunctuation(words[idx+(3+base)],[]) in months:
                        
                        opDate = " ".join([opDate," - ", str(words[idx+(2+base)]), str(removePunctuation(words[idx+(3+base)],[]))])
                        print("SPECIAL OP DATED: " + opDate)
                        base +=3
                    idx = idx+base
                        
                    #opDate = " ".join([opDate,cleanWord,year])
                    
                    if opCount == 0:
                        flashCurOp = curOp.split(" ")
                        opPart = flashCurOp[:len(flashCurOp)-trimCount]
                        #print("TrmiCount: " + str(trimCount) + " " + str(flashCurOp) + " " + str(opPart))
                        curOp = " ".join(opPart)
                        curOp = curOp.replace(":", "")
                        opCount = 1
                    writeJob(sname,opDate,curOp,experiment)
                    opDate = None
                    #reset = True
                else:
                    curOp = " ".join([curOp,word])
            elif opCount == 1 and looksLikeDay(cleanWord) or looksLikeYear(word) or word in ["-", "~", "="]:
                pass
#                 else: 
#                     opCount = 1
#                     if word not in string.punctuation:
#                         curOp = word
#                     reset = False
            else:
                if opCount == 1:
                    curOp = word
                else: 
                    curOp = " ".join([curOp,word])
                opCount = 0
                    
            idx+=1    
        if opDate:
            writeJob(sname,opDate,curOp,experiment)
#         
#         
#         
#         stextTrim = stext.split(":",1)
#         if len(stextTrim) > 1: 
#             parts = stextTrim[1].split(":")
#             op = ""
#             opDate = ""
#             for pidx, part in enumerate(parts):
#                 
#                 print("Part to test is: " + part)
#                 if pidx == 0: # first one
#                     op = part
#                 else: # Need to eat away at the part until you get to the end of the dates.
#                     words = part.strip().split(" ")
#                     expectDay = True
#                     expectDashOrMonth = False
#                     checkYear = False
#                     
#                     wordCount = len(words)
#                      
#                     idx = 0 
#                     skip = False
#                     for idx, word in enumerate(words):
#                         if skip:
#                             pass
#                         else:
#                             if expectDay and looksLikeDay(word):
#                                 opDate = word
#                                 expectDashOrMonth = True
#                                 expectDay = False
#                             elif expectDashOrMonth:
#                                 cword = removePunctuation(word,[])
#                                 if cword in months:
#                                     opDate = " ".join([opDate,cword])
#                                     checkYear = True
#                                 elif word in ["-","~"]:
#                                     opDate = " ".join([opDate,"-"]) 
#                                     expectDay = True
#                                 expectDashOrMonth = False   
#                             elif checkYear:
#                                 checkYear = False
#                                 if looksLikeYear(word):
#                                     opDate = " ".join([opDate,word[0:4]])
#                                     #print("1: " + opDate + " | " + op)
#                                     writeJob(sname,opDate,op,experiment)
#                                     expectDay = True
#                                 elif looksLikeDay(word):
#                                     #print("2: " + opDate + " | " + op)
#                                     writeJob(sname,opDate,op,experiment)
#                                     opDate = word
#                                     expectDashOrMonth = True
#                                 else: #no longer processing a date
#                                     writeJob(sname,opDate,op,experiment)
#                                     skip = True
#                                     newOp = " ".join(words[idx:])
#                                 #    print("Aidx: "  + str(idx) + " cur op = " + op + " new op " + newOp)
#                                     op = newOp
#                             else:
#                                 skip = True
#                                 newOp = " ".join(words[idx-1:])
#                                 #print("Bidx: "  + str(idx) + " cur op = " + op + " new op " + newOp)
#                                 op = newOp
#                                     
#             writeJob(sname,opDate,op,experiment)               
#         #print (stext)
#         #parts = stext.split(" ") # chunk everything into words
#         
#         curDate = None
#         expectDay = False
#         expectDayOrMonth = False
#         testYear = False
#         #corrected = correctWords(parts,corrections)
#         #rawwords = corrected.split(" ")
#         #words = list(filter(None,rawwords))
#         prevOp = ""
#         curOp = ""
#         words = stext.split(" ")
#         for word in words:
#             word = word.strip()
#             if testYear:
#                 #yearMatch = re.search("[0-9]{4}", word) 
#                 print(curDate)
#                 if (word == "-" or word == "="):
#                     print ("dash up")
#                     curDate = " ".join([str(curDate),str("-")])
#                     testYear = False
#                     expectDayOrMonth = True
#                 elif looksLikeYear(word):
#                     #curDate = " ".join([str(curDate),str(yearMatch.group(0))])
#                     curDate = " ".join([str(curDate),str(word)])
#                     writeJob(sname,curDate,curOp, prevOp, experiment)
#                     testYear = False
#                     expectDay = False
#                     prevOp = curOp if curOp else prevOp
#                     curOp = ""
#                 elif word in months: # same operation, different date
#                     writeJob(sname,curDate,curOp, prevOp, experiment)
#                     expectDay = True
#                     testYear = False
#                     prevOp = curOp if curOp else prevOp
#                     curDate = word
#                 else: # new operation
#                     writeJob(sname,curDate,curOp, prevOp, experiment)
#                     curDate = None
#                     prevOp = curOp if curOp else prevOp
#                     curOp = word 
#                     expectDay = False
#                     testYear = False
#             elif expectDayOrMonth:# this case is for after a dash
#                 if word in months:
#                     expectDay = True
#                     curDate = " ".join([str(curDate),str(word)])
#                 else: 
#                     curDate = " ".join([str(curDate),str(word).strip()])
#                     testYear = True
#                     expectDay = False
#                 expectDayOrMonth = False
#             elif expectDay:
#                 curDate = " ".join([str(curDate),str(word).strip()])
#                 testYear = True
#                 expectDay = False
#             elif word in months: # same operation, different date
#                 expectDay = True
#                 testYear = False
#                 curDate = word
#             else:
#                 expectDay = False
#                 testYear = False
#                 curOp = " ".join([curOp,word])
#         if curDate != "None":
#             writeJob(sname,curDate,curOp, prevOp, experiment)


        
year = ""
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\BroadbalkOperations.txt", "w+", 1)
fileList = os.listdir("D:\\work\\yieldbooks\\Broadbalk")
fileList.sort()

corrections = []
with open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\corrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())

months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec", "Mey") # Note Mey as seems to be a problem catching correction
print("starting Broadbalk")
allLines = []
prevlines = []
for idx, fname in enumerate(fileList):
    nyear = fname[0:4]
    
    print("idx: " + str(idx) + ":  nyear = " + nyear + ", year =  " + year)
    if int(nyear) >= 1968 and fname.endswith(".jpg"): 
        print("processing document " + str(idx) + ", " +fname)
        page = getPageScan("D:\\work\\yieldbooks\\Broadbalk\\" + fname)
        page = re.sub(" +"," ",page).strip()
        lines = toCorrectedLines(page)        
        #print("allLines " + str(len(allLines)))
        #if len(allLines) == 0:
        #    print("first page")
        #    allLines = prevlines
        #    year = nyear
        allLines = allLines + prevlines
        print("lines size " + str(len(lines)))
        print("allLines size " + str(len(allLines)))
        if nyear != year:
            getOperations(allLines)
            year = nyear
            allLines = []
        
        prevlines = lines
# finalise last
getOperations(allLines)
print('done')
ofOperations.close()