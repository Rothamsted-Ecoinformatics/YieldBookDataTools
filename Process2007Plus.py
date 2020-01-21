'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to attract the experimental diary

@author: ostlerr
'''
import os
from YieldBookToData import * 
import configparser
import xmltodict

class Job():
    def __init__(self):
        self.date = None
        self.description = None
        self.section = None
        self.jobType = None
        self.rate = None
        self.rateUnit = None

def applyCorrections(content):
    # Note this preserves lines as they provide structural cues to help with processing
    # some special force replacements - these could be applied to the whole doc
    content = re.sub(r"tm\)([\w])",r"tm \1",content).strip().replace("tm ","tm) ")
    #content = content.replace("~","-")
    return correctWords(content)

def writeJob(job):    
    outfile.write("|".join([str(experiment),str(year),str(job.date),str(job.jobType),str(job.section),str(job.description),str(job.rate),str(job.rateUnit)]))
    outfile.write("\n")
        
def testLast(job):
    parts = job.description.split(" ")
    #print(parts)
    if (len(parts)-1) > 0:
        testlen = len(parts)
        p2 = parts[testlen-2].replace(".","")
        p3 = parts[testlen-3].replace(".","")
        print(p2 + " : " + p3)
        if re.match(r"[\d]+\.?[\d]?",p2):
            job.rate = parts[testlen-2]
            job.rateUnit = parts[testlen-1]
            job.description = " ".join(parts[:testlen-2])
        elif re.match(r"[\d]+\.?[\d]?",p3):
            job.rate = parts[testlen-3]
            job.rateUnit = " ".join([parts[testlen-2],parts[testlen-1]])
            job.description = " ".join(parts[:len(parts)-3])
        else:
            job.description = " ".join(parts)
    return job    

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['oe_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
year = ""
section = ""

with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    
    year = rep["year"]
    if int(year) >= 2007:
        print("start processing year: " + str(year))
        content = rep["rawcontent"]        
        content = applyCorrections(content)
                
        curSection = ""
        lines = content.split("\n")
        for line in lines:
            # this only has operations data so no need to find the diary records. Each record is single line
            # if the first character is a digit then it is a date otherwise a section heading 
            if line[0].isdigit():
                parts = line.split(" ",2)
                job = Job()
                job.date = parts[0]
                job.jobType = parts[1]
                job.description = parts[2].strip()
                job.section = curSection
                job = testLast(job)
                writeJob(job)
            else:
                curSection = line.strip() 
                    