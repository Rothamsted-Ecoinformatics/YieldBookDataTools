'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to extract the experimental diary

@author: ostlerr
'''
import os
from imageToText.YieldBookToData import checkForSection, checkJobDate, getPageScan, toCorrectedLines
import configparser
import re

specialSection = ""

def writeJob(sname,curOpDate,curOp,curOpType):
    if len(curOp) > 1:
        outfile.write("|".join([str(experiment),str(year),str(sname),str(curOpDate),str(curOp),curOpType]))
        outfile.write("\n")

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
strSections = config['EXPERIMENT']['sections']
sectionNames = strSections.split(",") if len(strSections) > 0 else []
year = ""
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
        lines = toCorrectedLines(page)
                
        for line in lines:
            if line.lower().startswith("experimental diary"):
                processingDiary = True
            elif processingDiary:
                isNewSection, nsname = checkForSection(line,sectionNames)    
                if isNewSection:
                    sname= nsname
                else: #processing diary entries here
                    isDate, opDate, job = checkJobDate(line)
                    if job.startswith("Note:"):
                        processingDiary = False
                    elif isDate:
                        curOp = curOp.replace(";",":")
                        curOp = curOp.replace(": B :","||")
                        curOp = curOp.replace(": T :","||")
                        curOp = curOp.replace(": tm)","||")
                        curOps = curOp.split("||")
                        for co in curOps:
                            writeJob(sname,curOpDate,co,curOpType)
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
        
outfile.close()