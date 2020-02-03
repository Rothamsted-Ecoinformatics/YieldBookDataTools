'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to extract the experimental diary

@author: ostlerr
'''
import os
from YieldBookToData import correctWords
import configparser
import re
import xmltodict

def writeJob(sname,curOpDate,curOp):
    if len(curOp) > 1:
        outfile.write("|".join([str(experiment),str(year),sname.strip(),curOpDate.strip(),curOp.strip()]))
        outfile.write("\n")

def applyCorrections(content):
    # Note this preserves lines as they provide structural cues to help with processing
    # some special force replacements - these could be applied to the whole doc
    content = re.sub(r"tm\)([\w])",r"tm \1",content).strip().replace("tm ","tm) ")
    #content = content.replace("~","-")
    return correctWords(content)

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['oc_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
year = ""

with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    
    year = rep["year"]
    if int(year) >=1992 and int(year) <= 2006: # need to check formats before running this    
        print("start processing year: " + str(year))
        content = rep["rawcontent"]        
        content = applyCorrections(content)
                
        curOpDate = ""
        curSection = ""
        lines = content.split("\n")
        for line in lines:
            # this only has operations data so no need to find the diary records. Each record is single line
            parts = re.split(r": [TB] :",line)
            print(parts)
            if len(parts) == 2: #date and operation
                if parts[0]:
                    curOpDate = parts[0]
                writeJob (curSection,curOpDate,parts[1])
            else:
                curSection = line.strip() 
outfile.close()