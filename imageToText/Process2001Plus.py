'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to attract the experimental diary

@author: ostlerr
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import * 
import re

outfile = None
sectionStarts = ()
sectionNames = ()
experiment = None
corrections = []
specialSection = ""
year = ""
    
class job():
    def __init__(self):
        self.date = None
        self.description = None
        self.section = None
        self.jobType = None
        self.rate = None
        self.rateUnit = None
    
#with open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\corrections.csv", 'r') as infile:
#    for line in infile:
#        corrections.append(line.strip())

#months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")

def globals(poutfile,pexperiment,pSections):   
    global outfile
    global experiment
    global sectionNames
    outfile = poutfile
    experiment = pexperiment
    sectionNames = pSections

def tidyUp(messyPage):
    messyPage = messyPage.replace("\n\n","\n")
    messyPage = re.sub("[0-9]{1,2}- ?[\w]+- ?[0-9]{2}",clearSpace, messyPage) # this cleans up spaces from dates
    messyPage = messyPage.replace("{","f") # Doesn't always do a good job with f)
    return messyPage            

def printJobs(jobs):
    
    for job in jobs:
        outfile.write("|".join([experiment,str(year),str(job.date),str(job.jobType),str(job.section),str(job.description),str(job.rate),str(job.rateUnit)]))
        outfile.write("\n")

def checkForSection(line):
    lline = removePunctuation(line.lower(),[])
    for name in sectionNames:
        if lline.startswith(name):
            return name
    return None
        
def testLast(job, parts):
    testUnit = parts[len(parts)-1]
    testlen = len(testUnit)
    
    if testUnit[testlen-2:] == "ha" or testUnit[testlen-2:testlen-1] == "m":
        job.rate = parts[len(parts)-2]
        job.rateUnit = testUnit
        job.description = " ".join(parts[:len(parts)-2])
    else:
        job.description = " ".join(parts)
    return job    

def loopDocs(dir):
    global year
    fileList = os.listdir(dir)
    sorted(fileList)
    jobs = []
    section = ""
    curJob = None
    for fname in fileList:
        nyear = fname[0:4]
        if int(nyear) > 2000 and fname.endswith(".jpg"): 
            page = getPageScan(dir + "\\" + fname)
            if nyear != year:
                printJobs(jobs)
                jobs = []
                year = nyear
            if page:
                if page.find("Experimental Diary") > -1:
                    page = page[page.find("Experimental Diary")+19:] # this should stop everything before the Cultivations from being processed
                    section = ""
                if page.find("YIELDS") > -1:
                    page = page[:page.find("YIELDS")]    
                page = tidyUp(page)
                dirtyJobs = page.split("\n")
                    
                curDate = ""
                
                curJob = None
                for line in dirtyJobs:
                    print("original : " + line)
                    isNewSection = checkForSection(line)
                    if isNewSection:
                        section = isNewSection
                        if curJob:
                            jobs.append(curJob)
                            curJob = None
                    elif not line or len(line) == 0 or line.find("Cropped sections") > 1 or line.lower().find("rate unit") > 1:
                        pass
                    else:
                        parts = line.split(" ")
                        dateMatch = re.search("\d{1,2}[-|\/][\w\d]+[-|\/]\d{2,4}",parts[0])
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
                            curJob = testLast(curJob,parts[2:])
                            curJob.section = section        
                        elif len(parts[0]) <=2 and parts[0][0] in ("a","s","p","f"):
                            print("++++++++++++++")
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
    if curJob:
        jobs.append(curJob)
    printJobs(jobs)                        
print('done')