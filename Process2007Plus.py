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

class job():
    def __init__(self):
        self.date = None
        self.description = None
        self.section = None
        self.jobType = None
        self.rate = None
        self.rateUnit = None

def tidyUp(messyPage):
    messyPage = messyPage.replace("\n\n","\n")
    messyPage = re.sub("[0-9]{1,2}- ?[\w]+- ?[0-9]{2}",clearSpace, messyPage) # this cleans up spaces from dates
    messyPage = messyPage.replace("{","f") # Doesn't always do a good job with f)
    return messyPage            

def printJobs(jobs):
    
    for job in jobs:
        outfile.write("|".join([str(experiment),str(year),str(job.date),str(job.jobType),str(job.section),str(job.description),str(job.rate),str(job.rateUnit)]))
        outfile.write("\n")

def checkForSection(line):
    lline = removePunctuation(line.lower(),[])
    for name in sectionNames:
        if lline.startswith(name):
            return line
    return None
        
def testLast(job, parts):
    if (len(parts)-1) > 0:
        #testUnit = parts[len(parts)-1]
        testlen = len(parts)
        p2 = parts[testlen-2].replace(".","")
        p3 = parts[testlen-3].replace(".","")
        if p2.isdigit():
            job.rate = parts[testlen-2]
            job.rateUnit = parts[testlen-1]
            job.description = " ".join(parts[:testlen-2])
        elif p3.isdigit():
            job.rate = parts[testlen-3]
            job.rateUnit = " ".join([parts[testlen-2],parts[testlen-1]])
            job.description = " ".join(parts[:len(parts)-3])
        else:
            job.description = " ".join(parts)
    return job    

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['od_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
strSections = config['EXPERIMENT']['sections']
sectionNames = strSections.split(",")
sectionStarts = ()
specialSection = ""
year = ""
print(sectionNames)
jobs = []
section = ""
curJob = None
year = ""
with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    
    year = rep["year"]
    #if int(nyear) >= 2007 and fname.endswith(".jpg"): 
    if int(year) >= 2007:
        content = rep["rawcontent"]       
        
        jobs = []
        #year = nyear
    
        if content.find("Experimental Diary") > -1:
            content = content[content.find("Experimental Diary")+19:] # this should stop everything before the Cultivations from being processed
            section = ""
        if content.find("YIELDS") > -1:
            content = content[:content.find("YIELDS")]  
        elif content.find("Grain and straw tonnes") > -1:
            content = content[:content.find("Grain and straw tonnes")]        
        content = tidyUp(content)
        dirtyJobs = content.split("\n")
            
        curDate = ""
        
        curJob = None
        for line in dirtyJobs:
            print("original : " + line)
            isNewSection = checkForSection(line)
            if isNewSection:
                print("b")
                section = isNewSection
                if curJob:
                    jobs.append(curJob)
                    curJob = None
            elif not line or len(line) == 0 or line.find("Cropped sections") > 1 or line.lower().find("rate unit") > 1:
                pass
            else:
                parts = line.split(" ")
                dateMatch = re.search("\d{1,2}[-|\/][\w\d]+[-|\/]\d{2,4}",parts[0])
                #isMix = False # Not going to worry about this as only affects  2012/13
                #if line.find("@") > -1: # this is a bit tedious, ideally want to get each in as a new row
                #    isMix = True
                
                if dateMatch:
                    if curJob:
                        jobs.append(curJob)
                    curJob = job()
                    curJob.date = parts[0]
                    curDate = parts[0]
                    tjobtype = parts[1].strip()
                    if len(tjobtype)> 0:
                        curJob.jobType = tjobtype[0]
                    else:
                        curJob.jobType = "x"
                    curJob = testLast(curJob,parts[2:]) #2 for 2007+
                    curJob.section = section        
                    
                elif len(parts[0]) <=2 and parts[0][0] in ("a","s","p","f"):
                    if curJob:
                        jobs.append(curJob)
                    curJob = job()
                    curJob.date = curDate
                    curJob.jobType = parts[0][0]
                    curJob = testLast(curJob,parts[1:])
                    curJob.section = section
                else:
                    if curJob:
                        curJob.description = curJob.description + " " + line
        printJobs(jobs)
        
#if curJob:
#    jobs.append(curJob)
printJobs(jobs)                        