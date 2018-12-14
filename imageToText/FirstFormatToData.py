'''
Created on 3 Dec 2018

@author: ostlerr
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
import string
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from collections import namedtuple
import pandas as pd

cultivationsSegment = []
code = ""
title = ""
hasMetadata = False
inCultivations = False

def removePunctuation(value):
    result = ""
    for c in value:
        if c not in string.punctuation:
            result += c
    return result

def getMetadata(page,fname,pageIdx): # should only be in here if we have no metadata       
    lines = page.split("\n")
    design = "" 
    plots = ""
    sponsors = ""
    treatments = ""
    basal = ""
    global hasMetadata
    global code
    global title
    global inCultivations
    global cultivationsSegment
    section = 0 
    
    for idx, p in enumerate(lines):
        if p and section >= 0:
            testLine = correctLine(p.lower())
            lineParts = testLine.split(" ")
            if lineParts[0] == "cultivations": #fuzz.token_set_ratio(p,"Cultivations, etc.:") >= 75:# and hasMetadata:         
                design = correctWords(design.split(" "), corrections)
                plots = correctWords(plots.split(" "), corrections)
                treatments = correctWords(treatments.split(" "), corrections)
                sponsors = correctWords(sponsors.split(" "), corrections)
                ofMetadata.write("|".join([fname,str(pageIdx),code,title,year,str(design),str(sponsors),str(plots),str(treatments)]))
                ofMetadata.write("\n")   
                section = -1 # need to stop processing metadata
                # go and process the cultivations
                cultivationLines = lines[idx:]
                inCultivations = True
                getOperations(cultivationLines,fname,idx)
            elif(lineParts[0] == "sponsor"):
                section= 2
                hasMetadata = True
                sponsors = p
            elif(len(lineParts) >= 3 and lineParts[0] == "system" and lineParts[2] == "replication"):
                section= 3
                hasMetadata = True
                design = p
            elif(len(lineParts) >= 5 and lineParts[0] == "area" and (lineParts[3] == "plot" or lineParts[4] == "plot")):
                section= 4
                hasMetadata = True
                plots = p
            elif(lineParts[0] == "treatments"):
                section= 5
                hasMetadata = True
                treatments = p
            elif(lineParts[0] == "basal"):
                section = 6
                basal = p
            else: # means we're processing something
                if (section == 2):
                    sponsors = " ".join([sponsors, p.strip()])
                elif (section == 3):
                    design = " ".join([design, p.strip()])
                elif (section == 4):
                    plots = " ".join([plots, p.strip()])
                elif (section == 5):
                    treatments = " ".join([treatments, p.strip()])
                elif (section == 6):
                    basal = " ".join([basal, p.strip()])   
        elif p.isupper(): #Whoa there! got another experiment on the page
            cultivationsSegment = []
            title = p
            section = 0 # need to start processing again

def correctLine(line):
    correctedLine = correctWords(line.split(),paragraphStartKeyWords)
    return correctedLine

# Note there is a bias based on word length = e.g. 3 letter word gives score 67 if just one change. Should also ignore 2 letter words
def correctWords(words,dictionary):
    #cutoffs = {3:67, 4:75, 5:80}
    newWords = []
    for word in words:
        wordLen = len(word)
        if wordLen <= 2 or word in exclusions:
            newWords.append(word)
        else:
            cutOff=80
            if wordLen == 3:
                cutOff = 66
            elif (wordLen == 4):
                cutOff = 74
                
            matched = process.extractOne(word,dictionary,scorer=fuzz.token_set_ratio,score_cutoff=cutOff)
            if matched:
                newWords.append(matched[0])
            else:
                newWords.append(word)
    return " ".join(newWords)
    
# this method is all about finding the end of a cultivations segment. If no end is found by the end of the page then carries through to the next page    
def getOperations(lines,fname,pageIdx):
    global cultivationsSegment
    global code
    global title
    global inCultivations
    crapCount = 0;
    for idx, line in enumerate(lines):
        if (inCultivations):
            if(fuzz.token_set_ratio(line,"Cultivations, etc.:") >= 75): 
                cultivationsSegment.clear()
                inCultivations = True
                parts = line.split(" ")
                if (len(parts) >2):
                    line = " ".join(parts[2:])
                    cultivationsSegment.append(line)
            elif(inCultivations):
                if (len(line) < 10):
                    crapCount += 1;
                else:
                    crapCount = 0
                    
                if(fuzz.token_set_ratio(line,"Rothamsted") > 75):
                    cultivationsSegment.append("Rothamsted")
                elif(fuzz.token_set_ratio(line,"Woburn") > 75):
                    cultivationsSegment.append("Woburn")
                elif(fuzz.ratio(line,"Summary of Results") > 80 or fuzz.ratio(line,"Standard errors") > 80 or fuzz.token_set_ratio(line,"Note") >= 80  or crapCount > 5):    
                    processCultivations(fname,pageIdx)
                    inCultivations = False
                    print("ex cultivations")
                else:
                    cultivationsSegment.append(line)
    
def writeJob(fname,pageIdx,sname,curDate,curOp,prevOp):
    global code
    global title
    cleanCurDate = removePunctuation(str(curDate))
    if not curOp:   
        curOp = prevOp
    if curOp:
        ofOperations.write("|".join([fname,str(pageIdx),code,title,year,str(sname),cleanCurDate,str(curOp).strip()]))
        ofOperations.write("\n")    
            
#this method is about subsectioning the cultivations then writing them             
def processCultivations(fname,pageIdx):   #cultivationSections = cultivationsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    #print("cultivation sections = " + str(len(cultivationSections)))
    sectionName = ""
    subsections = {}
    subsectionText = ""
    centre=""
    
    for line in cultivationsSegment:
        parts = re.split(r"[:.,]",line,1)
        
        matched = process.extractOne(parts[0],sectionKeywords,scorer=fuzz.partial_ratio,score_cutoff=85)
        if (matched):
            if(sectionName): # add the old section name to the dictionary. Length check is for misidentifications - sub sections should be short
                subsections[sectionName] = subsectionText
            sectionName = " ".join([centre,parts[0]]).strip()
            subsectionText = "" #set up the new section text
            if(parts and len(parts) > 1):
                line = parts[1]
        elif(line == "Woburn"):
            centre = "Woburn"
            line = ""
        elif(line == "Rothamsted"):
            centre = "Rothamsted"
            line = ""
        
        if (len(line) > 1):
            subsectionText = " ".join([str(subsectionText),line])
    if not sectionName:
        sectionName = "All plots"
    subsections[sectionName] = subsectionText           # got a new section...probably
    
    # Now process the subsections:
    print("WRITING JOBS:")
    for sname, stext in subsections.items():
        parts = stext.split(" ") # chunk everything into words
        
        curDate = None
        expectDay = False
        testYear = False
        corrected = correctWords(parts,corrections)
        rawwords = corrected.split(" ")
        words = list(filter(None,rawwords))
        prevOp = ""
        curOp = ""
        for word in words:
            word = word.strip()
            
            if word == "and": 
                print("skip")
            elif testYear:
                yearMatch = re.search("[0-9]{4}", word) 
                if (yearMatch):
                    curDate = " ".join([str(curDate),str(yearMatch.group(0))])
                    writeJob(fname,pageIdx,sname,curDate,curOp, prevOp)
                    testYear = False
                    expectDay = False
                    prevOp = curOp
                elif word in months: # same operation, different date
                    writeJob(fname,pageIdx,sname,curDate,curOp, prevOp)
                    expectDay = True
                    testYear = False
                    prevOp = curOp
                    curDate = word
                else: # new operation
                    writeJob(fname,pageIdx,sname,curDate,curOp, prevOp)
                    curDate = None
                    prevOp = curOp
                    curOp = word 
                    expectDay = False
                    testYear = False
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
        writeJob(fname,pageIdx,sname,curDate,curOp, prevOp)
    
def getExperimentCodeAndName(page,fname,pageIdx):
    global code
    global title
    global hasMetadata
    rawlines = page.split("\n")
    lines = list(filter(None,rawlines))
    localCode = ""
    localTitle = ""
    
    for idx in range(3):
        line = lines[idx]
        if idx == 0:
            localCode = line
        elif idx == 1 and line and line.isupper(): # will assume always on second line
            localTitle = line 
        elif idx == 2 and line:
            if localTitle and localTitle.lower() in crops:
                localTitle = ": ".join([localTitle, lines[2]])
                
    if localTitle: # expect this to be a new experiment, therefore reset and look out for metadata
        if (inCultivations): #necessary in case last page finished with cultivations and now on a new experiment
            processCultivations(fname,pageIdx)
            cultivationsSegment = []
        title = localTitle
        code = localCode
        hasMetadata = False
            
year = "1952"
ofOperations = open("operations" + year + ".txt", "w+", 1)
ofMetadata = open("metadata" + year + ".txt", "w+", 1)
ofBasal = open("basalManuring" + year + ".txt", "w+", 1)
fileList = os.listdir("D:\\yieldbooks\\" + year)

fileList.sort()

exclusions = ("and")

# not working
corrections = []
with open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\corrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())
print (corrections)
#corrections = ("cwt","Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec","ammonia", "all","Little","Hoos","again","Ashwells","late","flowering","M.C.P.A", "MCPA","D.N.O.C","DNOC","13/4","Nitrochalk","grazed","grazing","Highfield","series","rabbit","Krilium","experiment","beet","Majestic","Red","Plumage","earthed","potatoes" "barley","seed","autumn","ploughed", "variety", "Squareheads", "fertilizers", "applied", "nitrate", "fallow","per","acre")


paragraphStartKeyWords = ("system", "replication","basal","manuring","area","each","plot","cultivations")

sectionKeywords = ("cropped plots", "fallow plots","crop sections","block","fallow section","green manures", "cabbages","barley", "sugar beet", "clover", "wheat", "potatoes", "rye", "ley", "globe beet", "spring cabbages", "leeks")
months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
crops = ("spring beans", "potatoes", "wheat", "barley", "lucerne", "broad beans", "spring oats", "globe beet", "sugar beet", "permanent grass")

for idx, fname in enumerate(fileList):
    
    if fname.endswith(".jpg") and idx > 3: 
        print("processing document " + str(idx) + ", " +fname)
        
        page = getPageScan("D:\\yieldbooks\\" + year + "\\" + fname)
        page = re.sub(" +"," ",page).strip()
        getExperimentCodeAndName(page,fname,idx)
        if inCultivations:
            getOperations(page,fname,idx)
        if not hasMetadata:
            getMetadata(page,fname,idx)
        
print('done')
ofOperations.close()
ofMetadata.close()
ofBasal.close()