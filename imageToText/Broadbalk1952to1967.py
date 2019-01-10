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
        if (fuzz.token_set_ratio(line,"Broadbalk Wilderness") >= 80):
            processCultivations(expt)
            expt = "Broadbalk Wilderness"
            cultivationsSegment.clear()
        elif(fuzz.token_set_ratio(line,"Cultivations, etc.:") >= 75): 
            
            cultivationsSegment.clear()
            inCultivations = True
            parts = line.split(" ")
            if (len(parts) >2):
                line = " ".join(parts[2:])
                cultivationsSegment.append(line)
        elif(inCultivations):
            # Need to do something with notes    
            if(fuzz.ratio(line,"Summary of Results") > 80 or fuzz.ratio(line,"Standard errors") > 80):    
                processCultivations(expt)
                inCultivations = False
                print("ex cultivations")
            else:
                cultivationsSegment.append(line)
    if (inCultivations):
        processCultivations(expt)
    
def writeJob(fname,pageIdx,sname,curDate,curOp,prevOp, expt):
    cleanCurDate = removePunctuation(str(curDate), ("-"))
    
    if not curOp:   
        curOp = prevOp
    if curOp:
        cleanCurOp = tidyOp(curOp)
        ofOperations.write("|".join([expt,year,str(sname),cleanCurDate,cleanCurOp]))
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
    print (page)
    lines = page.split("\n")
    cleanLines = []
    for line in lines:
        rawwords = line.split(" ") # chunk everything into words
        corrected = correctWords(rawwords,corrections)
        print(corrected)
        cleanwords = corrected.split(" ")
        words = list(filter(None,cleanwords))
        print("words: " + str(words))
        cleanLine = " ".join(words)
        print("cleanLine: " + cleanLine)
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
    print("WRITING JOBS:")
    processSections(experiment,subsections)
        
def processSections(experiment,subsections):
    for sname, stext in subsections.items():
        #print (stext)
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
                    writeJob(sname,curDate,curOp, prevOp, experiment)
                    testYear = False
                    expectDay = False
                    prevOp = curOp if curOp else prevOp
                    curOp = ""
                elif word in months: # same operation, different date
                    writeJob(sname,curDate,curOp, prevOp, experiment)
                    expectDay = True
                    testYear = False
                    prevOp = curOp if curOp else prevOp
                    curDate = word
                else: # new operation
                    writeJob(sname,curDate,curOp, prevOp, experiment)
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
            writeJob(sname,curDate,curOp, prevOp, experiment)

        
year = ""
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\BroadbalkOperations.txt", "w+", 1)
fileList = os.listdir("D:\\work\\yieldbooks\\Broadbalk")
fileList.sort()

corrections = []
with open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\corrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())

months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
print("starting Broadbalk")
for idx, fname in enumerate(fileList):
    nyear = fname[0:4]
    if int(nyear) < 1968 and fname.endswith(".jpg"): 
        print("processing document " + str(idx) + ", " +fname)
        
        inCultivations = True if (nyear == year) else False
        year = nyear
        page = getPageScan("D:\\work\\yieldbooks\\Broadbalk\\" + fname)
        page = re.sub(" +"," ",page).strip()
        lines = toCorrectedLines(page)        
        getOperations(lines)
        
print('done')
ofOperations.close()