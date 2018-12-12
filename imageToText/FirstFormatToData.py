'''
Created on 3 Dec 2018

@author: ostlerr
'''
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

def getMetadata(page,fname,pageIdx):        
    lines = page.split("\n")
    objective = ""
    design = "" 
    plots = ""
    sponsors = ""
    treatments = ""
    hasMetadata = False
    global code
    global title
    section = 0 
    for idx, p in enumerate(lines):
        if(idx == 0):
            code = p
        elif (idx == 1):
            if not code and p:
                code = p
            elif p:
                title = p 
        elif (idx == 2):
            if not title and p:
                title = p
        elif (idx == 3 and p):
            objective = p
            section = 1
        
        print(str(idx) + ": " + p)
        if p:
            testLine = correctLine(p.lower())
            lineParts = testLine.split(" ")
            if fuzz.token_set_ratio(p,"Cultivations, etc.:") >= 75 and hasMetadata:         
                ofMetadata.write("|".join([fname,str(pageIdx),code,title,str(objective),year,str(design),str(sponsors),str(plots),str(treatments)]))
                ofMetadata.write("\n")   
                section = 0
            elif(lineParts[0] == "sponsor"):
                section= 2
                hasMetadata = True
                print("sponsor: " + testLine)
                sponsors = p
            elif(len(lineParts) >= 3 and lineParts[0] == "system" and lineParts[2] == "replication"):
                section= 3
                hasMetadata = True
                print("design: " + testLine)
                design = p
            elif(len(lineParts) >= 5 and lineParts[0] == "area" and (lineParts[3] == "plot" or lineParts[4] == "plot")):
                section= 4
                hasMetadata = True
                print("plot area: " + testLine)
                plots = p
            elif(lineParts[0] == "treatments"):
                section= 5
                hasMetadata = True
                print("treatments: " + testLine)
                treatments = p
            else: # means we're processing something
                if (section == 1):
                    objective = " ".join([objective, p.strip()]) 
                    print("OBJECTIVE: " + objective)
                elif (section == 2):
                    sponsors = " ".join([sponsors, p.strip()])
                elif (section == 3):
                    design = " ".join([design, p.strip()])
                elif (section == 4):
                    plots = " ".join([plots, p.strip()])
                elif (section == 5):
                    treatments = " ".join([treatments, p.strip()])   
    
      

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
                print(word + ": " + str(matched) + " cutOFF: " + str(cutOff))
                newWords.append(matched[0])
            else:
                newWords.append(word)
    return " ".join(newWords)
    
def getOperations(page,cultivations,fname,pageIdx):
    lines = page.split("\n")
    global cultivationsSegment
    global code
    global title
    basal = ""
    inBasal = False
    crapCount = 0;
    for idx, line in enumerate(lines):
        print(str(idx) + " " + line)
#         if not cultivations:
#             if idx == 0: # could be here but still in cultivations
#                 code = line
#                 print("code: " + line)
#             elif (idx == 1):
#                 title = line 
#                 print("title: " + line)   
#             elif (idx == 2 and not title):
#                 title = line
#                 print("line3: " + str(line))   
        
                
        if (cultivations or idx > 3):
            if(fuzz.token_set_ratio(line,"Basal manuring:") >= 80):
                parts = line.split(":.,")
                if (len(parts) >1):
                    basal = parts[1]
                inBasal = True
            elif inBasal:
                basal = " ".join([basal,line])
            elif(fuzz.token_set_ratio(line,"Cultivations, etc.:") >= 75): 
                inBasal = False
                # Need to reset titles
                code = line[0]
                title = lines[1] if lines[1] else lines[2] 
                
                cultivationsSegment.clear()
                #print("in cultivations due to {" + str(line) + "}")
                cultivations = True
                # need to remove the first two words (cultivations, etc)
                parts = line.split(" ")
                if (len(parts) >2):
                    line = " ".join(parts[2:])
                    cultivationsSegment.append(line)
            elif(cultivations):
                if (len(line) < 10):
                    crapCount += 1;
                else:
                    crapCount = 0
                    
                if(fuzz.token_set_ratio(line,"Rothamsted") > 75):
                    cultivationsSegment.append("Rothamsted")
                elif(fuzz.token_set_ratio(line,"Woburn") > 75):
                    cultivationsSegment.append("Woburn")
                elif(fuzz.ratio(line,"Summary of Results") > 80 or fuzz.ratio(line,"Standard errors") > 80 or fuzz.token_set_ratio(line,"Note") >= 80  or crapCount > 5):    
                    cultivations = False
                    processCultivations(fname,pageIdx)
                    print("ex cultivations")
                else:
                    cultivationsSegment.append(line)
            else:
                print(line)
            print("in cultivations: " + str(cultivations))
        if basal:
            ofBasal.write("|").join([fname,str(pageIdx),code,title,year,basal])
            ofBasal.write("\n")
    return cultivations
    
def writeJob(fname,pageIdx,code,title,sname,curDate,curOp):
    cleanCurDate = removePunctuation(str(curDate))
    ofOperations.write("|".join([fname,str(pageIdx),code,title,year,str(sname),cleanCurDate,str(curOp).strip()]))
    ofOperations.write("\n")    
            
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
    centre=""
    for line in cultivationsSegment:
        parts = re.split(r"[:.,]",line,1)
        #print(parts)
        matched = process.extractOne(parts[0],sectionKeywords,scorer=fuzz.partial_ratio,score_cutoff=85)
        #print(matched)
        if (matched):
            if(sectionName): # add the old section name to the dictionary. Length check is for misidentifications - sub sections should be short
                subsections[sectionName] = subsectionText
            #if (len(parts[0]) < 22):
            if (parts[0].lower().startswith(sectionKeywords)):
                sectionName = " ".join([centre,parts[0]]).strip()
            print(sectionName)
            subsectionText = ""
            if(parts and len(parts) > 1):
                line = parts[1]
            else: 
                print("1 line parts is: " + str(parts))
            
        elif(line == "Woburn"):
            centre = "Woburn"
            line = ""
        elif(line == "Rothamsted"):
            centre = "Rothamsted"
            line = ""
        
        if (len(line) > 1):
            subsectionText = " ".join([str(subsectionText),line])
            
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
        corrected = correctWords(parts,corrections)
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
        
    return expCode, expName

#try:
year = "1952"
ofOperations = open("operations" + year + ".txt", "w+", 1)
ofMetadata = open("metadata" + year + ".txt", "w+", 1)
ofBasal = open("basalManuring" + year + ".txt", "w+", 1)
fileList = os.listdir("V:\\YieldBook1952\\FullSize")

fileList.sort()

exclusions = ("and")
corrections = ("cwt","Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec","again","Ashwells","late","flowering","series","rabbit","Krilium","experiment","beet" "Majestic","Red","Plumage","earthed","potatoes" "barley","seed","autumn","ploughed", "variety", "Squareheads", "fertilizers", "applied", "nitrate", "fallow","per","acre")
paragraphStartKeyWords = ("system", "replication","basal","manuring","area","each","plot")

sectionKeywords = ("cropped plots", "fallow plots","crop sections","fallow section","green manures", "cabbages","barley", "sugar beet", "clover", "wheat", "potatoes", "rye", "ley", "globe beet", "spring cabbages", "leeks")
months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")

inCultivations = False
for idx, fname in enumerate(fileList):
    
    if fname.endswith(".jpg") and idx > 3: 
        print("processing document " + str(idx) + ", " +fname)
        print("Globals")
        print("code: " + str(code))
        print("title: " + str(title))
        
        page = getPageScan("V:\\YieldBook1952\\FullSize\\" + fname)
        page = re.sub(" +"," ",page).strip()
        
        getMetadata(page,fname,idx)
        inCultivations = getOperations(page,inCultivations,fname,idx)
        print("inCultivations: " + str(inCultivations))
        
print('done')
ofOperations.close()
ofMetadata.close()
ofBasal.close()