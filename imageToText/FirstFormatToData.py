'''
Created on 3 Dec 2018

@author: ostlerr
'''
import cv2
import numpy as np
import pytesseract
import re
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
from docutils.nodes import paragraph, Part
import string

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

cultivationsSegment = []
code = ""
title = ""

def removePunctuation(value):
    result = ""
    for c in value:
        if c not in string.punctuation:
            result += c
    return result

def getMetadata(page):        
    curEx = ""  
    #if (page.find("Object:") > -1):
        #sponsor = getSponsors(line)
    paragraphs = page.split("\n")
        #print(paragraphs)
        #curEx = paragraphs[0].strip()
        #title = paragraphs[1].strip()
        #objective = ""
        #design = "" 
       # plots = ""
        #treatments = ""
       # section = 0
    line = 1
    for p in paragraphs:
        print(str(line) + ": " + p)
        line +=1
#             
#             if (p.startswith("Object")):
#                 section= 1
#                 objective = (p.split(":")[1]).replace("\n", " ")
#             elif (p.startswith("Sponsor")):
#                 section= 2
#                 # do nothing
#             elif (p.startswith("Design")):
#                 section= 3
#                 design = (p.split(":")[1]).replace("\n", " ")
#             elif ((p.startswith("Areas") or p.startswith("Whole") or p.startswith("Plot")) and len(p.split(":"))==2):
#                 section= 4
#                 plots = (p.split(":")[1]).replace("\n", " ")
#             elif (p.startswith("Treatments")):
#                 section= 5
#                 # do nothing
#                 treatments = ""
#             else: # means we're processing something
#                 if (section == 1):
#                     objective = objective +" "+p.strip() 
#                 #if (section == 2):
#                     #sponsor = sponsor
#                 if (section == 3):
#                     design = design +" "+p.strip()
#                 if (section == 4):
#                     plots = plots +" "+p.strip()
#                 if (section == 5):
#                     treatments = treatments +" "+p.strip()   
        #foMetadata.write(curEx+"|"+title+"|"+objective+"|"+sponsor+"|"+design+"|"+plots)
        #foMetadata.write("\n")
    return curEx

# Note there is a bias based on word length = e.g. 3 letter word gives score 67 if just one change. Should also ignore 2 letter words
def correctWords(words):
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
                
            matched = process.extractOne(word,corrections,scorer=fuzz.token_set_ratio,score_cutoff=cutOff)
            if matched:
                print(word + ": " + str(matched) + " cutOFF: " + str(cutOff))
                newWords.append(matched[0])
            else:
                newWords.append(word)
        
            
    return " ".join(newWords)
    

def correctWords2(page,cultivations,fname,pageIdx):
    lines = page.split("\n")
    #print(str(len(rawlines)))
    #lines = list(filter(" ",rawlines))
    #print(str(len(lines)))
    global cultivationsSegment
    global code
    global title
    for idx, line in enumerate(lines):
        print(str(idx) + " " + line)
        if not cultivations:
            if idx == 0: # could be here but still in cultivations
                code = line
                print("code: " + line)
            elif (idx == 1):
                title = line 
                print("title: " + line)   
            elif (idx == 2):
                print("line3: " + str(line))   
        
        
        if (cultivations or idx > 3):
            if(fuzz.token_set_ratio(line,"Cultivations, etc.:") >= 75):
                cultivationsSegment.clear()
                #print("in cultivations due to {" + str(line) + "}")
                cultivations = True
                # need to remove the first two words (cultivations, etc)
                parts = line.split(" ")
                if (len(parts) >2):
                    line = " ".join(parts[2:])
                    cultivationsSegment.append(line)
            elif(cultivations):
                if(fuzz.token_set_ratio(line,"Rothamsted") > 75):
                    cultivationsSegment.append("Rothamsted")
                elif(fuzz.token_set_ratio(line,"Woburn") > 75):
                    cultivationsSegment.append("Woburn")
                    
                #print("sumary of results match:")
                #print(fuzz.ratio(line,"Summary of Results"))
                elif(fuzz.ratio(line,"Summary of Results") > 80 or fuzz.token_set_ratio(line,"Note") >= 80):    
                    cultivations = False
                    print("line 100")
                    processCultivations(fname,pageIdx)
                    print("ex cultivations")
                else:
                    cultivationsSegment.append(line)
            else:
                print(line)
            print("in cultivations: " + str(cultivations))    
        #if cultivations:
        #    print("line 200")
        #    processCultivations()
    return cultivations
    
def writeJob(fname,pageIdx,code,title,sname,curDate,curOp):
    cleanCurDate = removePunctuation(str(curDate))
    outfile.write("|".join([fname,str(pageIdx),code,title,str(sname),cleanCurDate,str(curOp).strip()]))
    outfile.write("\n")
    
            
def processCultivations(fname,pageIdx):   
    print("processing cultivations: ")
    print(cultivationsSegment)
    print("start processing cultivations:")
     
    #cultivationSections = cultivationsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    #print("cultivation sections = " + str(len(cultivationSections)))
    sectionName = None
    subsections = {}
    subsectionText = ""
    centre="Rothamsted"
    for line in cultivationsSegment:
        # split to lines:
        #lines = sections.split("\n")
        
        
        
        parts = re.split(r"[:.,]",line,1)
        #print(parts)
        matched = process.extractOne(parts[0],sectionKeywords,scorer=fuzz.partial_ratio,score_cutoff=85)
        #print(matched)
        if (matched):
            if(sectionName): # add the old section name to the dictionary
                subsections[sectionName] = subsectionText
            sectionName = " ".join([centre,parts[0]])
            print(sectionName)
            subsectionText = ""
            line = parts[1]
            
        elif(line == "Woburn"):
            centre = "Woburn"
            line = ""
        elif(line == "Rothamsted"):
            centre = "Rothamsted"
            line = ""
        #print(line)   
        if (len(line) > 0):
            subsectionText = " ".join([str(subsectionText),line])
            #split to words
            #words = line.split(" ")
            #if (fuzz.ratio(line,"sections") > 85) or len(words) <= 2):
               # words. 
    print("final section name: " + str(sectionName))
    if(sectionName): # add the old section name to the dictionary
        subsections[sectionName] = subsectionText           # got a new section...probably
    else:
        subsections["all plots"] = subsectionText
    # Now process the subsections:
    
    print("writing jobs:")
    for sname, stext in subsections.items():
        print("sname: " + sname)
        parts = stext.split(" ") # chunk everything into words
        curOp = ""
        curDate = None
        expectDay = False
        testYear = False
        corrected = correctWords(parts)
        words = corrected.split(" ")
        
        for word in words:
            word = word.strip()
            #print(str(word) + ": " + str(curOp) + " + " + str(curDate))
            
            if word == "and" or len(word) == 0: 
                # skip
                word = ""
            elif testYear:
                yearMatch = re.search("[0-9]{4}", word) 
                if (yearMatch):
                    curDate = " ".join([str(curDate),str(yearMatch.group(0))])
                    writeJob(fname,pageIdx,code,title,sname,curDate,curOp)
                    testYear = False
                    expectDay = False
                    curOp = ""
                elif word in months: # same operation, different date
                    writeJob(fname,pageIdx,code,title,sname,curDate,curOp)
                    expectDay = True
                    testYear = False
                    curDate = word
                else: # new operation
                    writeJob(fname,pageIdx,code,title,sname,curDate,curOp)
                    curDate = None
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
        writeJob(fname,pageIdx,code,title,sname,curDate,curOp)
    print("Subsections:") 
    print(subsections) 
    print("================")   
    


def getExperimentCodeAndName(testString):
    expCode = None
    expName = None
    #paragraphs = testString
    paragraphs = testString.split("\n")
    paragraphs = list(filter(None,paragraphs))
    #print(paragraphs)
    
    idx0 = paragraphs[0].strip()
    codeMatches = re.match("[0-9]{2}/[A-Za-z]{1,2}/[0-9]", idx0)
    if (codeMatches):
        expCode = codeMatches.group(0)
        expName = paragraphs[1].strip() + " " + paragraphs[2].strip()
    else:
        expName = paragraphs[0].strip() + " " + paragraphs[1].strip() 
        
    #print(str(expCode) + " - " + str(expName))   
    return expCode, expName

#try:
outfile = open("yieldbook1952.txt", "w+", 1)
fileList = os.listdir("D:\\Code\\python\\workspace\\YieldBookDataTools\\test data\\1952")

fileList.sort()

year = "1952"
exclusions = ("and")
corrections = ("cwt","Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec","Ashwells","late","flowering","Majestic","Red","earthed","potatoes" "barley","seed","autumn","ploughed", "variety", "Squareheads", "fertilizers", "applied", "nitrate", "fallow","per","acre")
paragraphStartKeyWords = ("Cultivations, etc.:", "Crop sections:","Fallow section:","System of replication:","Basal manuring:","Area of each plot:")
sectionKeywords = ("section", "Barley", "Sugar beet", "Clover", "Wheat", "Potatoes", "Rye", "Ley", "Globe beet", "Spring cabbages", "Leeks")
months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")

inCultivations = False
for idx, fname in enumerate(fileList):
    
    if fname.endswith(".jpg"): 
        print("processing document " + str(idx) + ", " +fname)
        print("Globals")
        print("code: " + str(code))
        print("title: " + str(title))
        
        # Need to reset globals?
        #cultivationsSegment = []
        
        page = getPageScan("D:\\Code\\python\\workspace\\YieldBookDataTools\\test data\\1952\\" + fname)
        page = re.sub(" +"," ",page).strip()
        #page = 
        inCultivations = correctWords2(page,inCultivations,fname,idx)
        print("inCultivations: " + str(inCultivations))
        #print(page)
       # getMetadata(page)
     
print('done')
outfile.close()