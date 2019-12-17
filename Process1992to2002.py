'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to extract the experimental diary

@author: ostlerr
'''
import os
from YieldBookToData import checkForSection, checkJobDate, startsWithSection, removeBlankLines, correctWords
import configparser
import re
import xmltodict

specialSection = ""

def tidyOp(op):
    op = op.strip()
    op = re.sub(r"^:\s","",op)
    op = re.sub(r"^-\s","",op)
    return(op)


def writeJob(sname,curOpDate,curOp,curOpType):
    if len(curOp) > 1:
        outfile.write("|".join([str(experiment),str(year),str(sname).strip(),str(curOpDate),tidyOp(curOp),curOpType]))
        outfile.write("\n")

def writeJobs(sname,curOpDate,curOp,curOpType):
    if len(curOp) > 1:
        if re.search(r"[:.>;]\s?[~—@PTBOo\d]{1,2}\s?[:.>;]",curOp): # this is to deal with multiple operations for one date
            curOps = re.split(r"[:.>;]\s?[~—@PTBOo\d]{1,2}\s?[:.>;]",curOp)
            for co in curOps:
                writeJob(sname,curOpDate,co,curOpType)
        elif re.search(r":\stm\)",curOp): # this is to deal with multiple operations for one date
            curOps = re.split(r":\stm\)",curOp)
            for co in curOps:
                writeJob(sname,curOpDate,co,curOpType)
        else:
            writeJob(sname,curOpDate,curOp,curOpType)

def applyCorrections(content):
    # Note this preserves lines as they provide structural cues to help with processing
    # some special force replacements - these could be applied to the whole doc
    #content = content.replace(": :",":")    
    content = re.sub(r"tm\)([\w])",r"tm \1",content).strip()
    content = content.replace("~","-")
    return correctWords(content)

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['oc_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
print(srcdoc)
strSections = config['EXPERIMENT']['sections']
sectionNames = strSections.split(",") if len(strSections) > 0 else []
year = ""
with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    
    year = rep["year"]
    if int(year) >=1992 and int(year) <= 2006: # need to check formats before running this    
        print("start processing year: " + str(year))
        content = rep["rawcontent"]        
        content = applyCorrections(content)
                
        sname = ""
        curOp = ""
        curOpDate = ""
        curOpType = ""
        job = ""
        processingDiary = False
        
        lines = content.split("\n")
        for line in lines:
            
            if line.startswith("experimental diary") or line == "experimental diary":# or line.lower().startswith("i diary"):
                processingDiary = True
            elif processingDiary:
                isNewSection, nsname = checkForSection(line,sectionNames)    
                if isNewSection:
                    writeJobs(sname,curOpDate,curOp,curOpType)
                    curOpDate = ""
                    curOp = ""
                    curOpType = ""
                    sname= nsname
                
                else: #processing diary entries here
                    isDate, opDate, job = checkJobDate(line)
                    if job.lower().startswith("note"):
                        processingDiary = False
                    elif isDate:
                        writeJobs(sname,curOpDate,curOp,curOpType)
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
                            if len(parts) >=3:
                                print(parts)
                                curOp = parts[2]
                    else:
                        curOp = " ".join([curOp,line])
                        
                   
        writeJob(sname,curOpDate,curOp,curOpType)
        
outfile.close()