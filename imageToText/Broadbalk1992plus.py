'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to attract the experimental diary

@author: ostlerr
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
import code
from numpy.lib.financial import rate

def tidyUp(messyPage):
    messyPage = messyPage.replace("\n\n","\n")
    messyPage = re.sub("[0-9]{1,2}- ?[\w]+- ?[0-9]{2}",clearSpace, messyPage) # this cleans up spaces from dates
    messyPage = messyPage.replace("{","f") # Doesn't always do a good job with f)
    return page            

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

def checkForSection(line):
    sectionNames = ("all sections", "fallow", "forage maize", "w. wheat", "w. oats", "w wheat", "w oats", "potatoes")
    lline = line.lower()
    for name in sectionNames:
        if lline.startswith(name):
            return True, name
    return False, None

def writeJob(sname,year,curOpDate,curOp,curOpType):
    if len(curOp) > 1:
        ofOperations.write("|".join(["Broadbalk",year,str(sname),curOpDate,curOp,curOpType]))
        ofOperations.write("\n")

corrections = []
with open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\corrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())

pageNum = 1
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\BroadbalkOperations1992.txt", "w+", 1)
fileList = os.listdir("D:\\work\\yieldbooks\\Broadbalk\\1992")
sorted(fileList)
curEx="" # set default
processingDiary = False
specialSection = ""
year = ""
for fname in fileList:
    print("**************\npageNum: " + str(pageNum) + "\n**************")
    
    nyear = fname[0:4]
    sname = ""
    curOp = ""
    curOpDate = ""
    curOpType = ""
    doneWheat = False
    processingDiary = False
    if int(nyear) >= 1992 and fname.endswith(".jpg"): 
        year = nyear
        page = getPageScan("D:\\work\\yieldbooks\\Broadbalk\\1992\\" + fname)
        page = re.sub(" +"," ",page).strip()
        lines = toCorrectedLines(page)
        
        print(lines)
        
        for line in lines:
            if line.lower().startswith("experimental diary"):
                processingDiary = True
            elif processingDiary:
                isNewSection, nsname = checkForSection(line)    
                if isNewSection:
                    sname= nsname
                    if sname == "w. wheat" and doneWheat:
                        processingDiary = False
                    elif sname == "w. wheat": 
                        doneWheat = True
                else: #processing diary entries here
                    isDate, opDate, job = checkJobDate(line)
                    if job.startswith("Note:"):
                        processingDiary = False
                    elif isDate:
                        writeJob(sname,year,curOpDate,curOp,curOpType)
                        opDate = opDate.strip()
                        if opDate.endswith("00"):
                            curOpDate = opDate.replace("00","2000")
                        else: 
                            curOpDate = opDate[:7] + "19" + opDate[7:]
                        parts = job.split(" ",3)
                        if len(parts) == 4:
                            curOpType = parts[1]
                            curOp = parts[3]
                        else:
                            curOpType = "".join(parts[0:1])
                            curOp = parts[2]
                    else:
                        curOp = " ".join([curOp,job])
                   
        writeJob(sname,year,curOpDate,curOp,curOpType)
print('done')
ofOperations.close()