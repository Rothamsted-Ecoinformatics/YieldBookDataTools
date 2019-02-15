'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to extract the experimental diary

@author: ostlerr
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
import configparser

year = None
outfile = None
#sectionStarts = ()
sectionNames = ()
experiment = None
corrections = []
specialSection = ""
    
with open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\corrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())

months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")

#def globals(poutfile,psectionNames,pexperiment):   
    #global outfile
    #global sectionNames
 #   global sectionStarts
   # global experiment
  #  outfile = poutfile
 #   sectionNames = psectionNames
  #  sectionStarts = psectionStarts
#    experiment = pexperiment

def tidyUp(messyPage):
    messyPage = messyPage.replace("\n\n","\n")
    messyPage = re.sub("[0-9]{1,2}- ?[\w]+- ?[0-9]{2}",clearSpace, messyPage) # this cleans up spaces from dates
    messyPage = messyPage.replace("{","f") # Doesn't always do a good job with f)
    return messyPage

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
    lline = line.lower()
    for name in sectionNames:
        if lline.startswith(name):
            return True, name
    return False, None

def writeJob(sname,curOpDate,curOp,curOpType):
    global year
    if len(curOp) > 1:
        outfile.write("|".join([str(experiment),str(year),str(sname),str(curOpDate),str(curOp),curOpType]))
        outfile.write("\n")

def loopDocs():
    global year
    fileList = os.listdir(srcdocs)
    fileList.sort()
    processingDiary = False
    for fname in fileList:
        nyear = fname[0:4]
        sname = ""
        curOp = ""
        curOpDate = ""
        curOpType = ""
        processingDiary = False
        if int(nyear) >= 1992 and int(nyear) <= 2006 and fname.endswith(".jpg"): 
            year = nyear
            page = getPageScan(srcdocs + "\\" + fname)
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
                    else: #processing diary entries here
                        isDate, opDate, job = checkJobDate(line)
                        if job.startswith("Note:"):
                            processingDiary = False
                        elif isDate:
                            writeJob(sname,curOpDate,curOp,curOpType)
                            opDate = opDate.strip()
                            dateParts = opDate.split("-")
                            if len(dateParts) == 3:
                                if dateParts[2][0] == "0":
                                    dateParts[2] = "20" + dateParts[2]
                                else:
                                    dateParts[2] = "19" + dateParts[2]
                                curOpDate = "-".join(dateParts)
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
                       
            writeJob(sname,curOpDate,curOp,curOpType)

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
strSections = config['EXPERIMENT']['sections']
sectionsNames = strSections.split(",")
loopDocs()