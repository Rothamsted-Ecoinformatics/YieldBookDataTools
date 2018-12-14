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

pageNum = 1
outfile = open("diary2007.txt", "w+", 1)

fileList = os.listdir("D:\\yieldbooks\\1952")
sorted(fileList)
curEx="" # set default
processingDiary = False
specialSection = ""
for fname in fileList:
    print("**************\npageNum: " + str(pageNum) + "\n**************")
    
    
    if fname.endswith(".jpg"): 
        page = getPageScan("D:\\yieldbooks\\1952\\" + fname)
        if page:
            pageCode = getCode(page)
            print("Processing: " + str(processingDiary))
            processingDiary = False if code != pageCode else processingDiary
            code = pageCode if code != pageCode else code
            
            print(code + " - " + pageCode + " - " + str(processingDiary))
            
            if (page.find("Experimental Diary") > -1 or processingDiary): # this page has the experimental diary:
                page = page[page.find("Experimental Diary")+19:] # this should stop everything before the Cultivations from being processed
                processingDiary = True
                page = tidyUp(page)
                dirtyJobs = page.split("\n")
                
                specialSectionLine = 1
                lastJob = ""
                lastDate = ""
                lastOpCode = ""
                lastJob = ""
                lastRate = ""
                lastUnit = ""
                for job in dirtyJobs:
                    #print("original : " + job)
                    if(job.find(":") >-1):
                        specialSection = job.split(":")[0]
                        specialSectionLine = 2
                    elif (job.lower().find("rate")>-1 and job.lower().find("unit")>-1):
                        print(job)
                        if(specialSectionLine == 2):
                            specialSection += " " + job.lower().split("rate")[0].strip()
                            specialSectionLine = 1
                        else:
                            specialSection = job.lower().split("rate")[0].strip()
                        print(specialSection)
                    else: # Should be processing a diary record
                        jobDate, job = getJobDate(job)
                        opCode, job = getOperationCode(job)
                        rate, units, job = getRateUnitsJob(job)
                        
                            
                        if(opCode): # this means we have a new record, so the old one should be printed
                            if(lastOpCode):
                                print(code + "|" + str(specialSection) + "|" + str(lastDate) + "|" + str(lastOpCode) + "|" + lastJob + "|" + str(lastRate) + "|" + str(lastUnit))
                            # values should be reset
                            if(rate):
                                lastRate = rate
                                lastUnit = units
                            else :
                                lastRate = None
                                lastUnit = None
                            if(jobDate): # this is for repeated dates
                                lastDate = jobDate
                            lastOpCode = opCode
                            lastJob = job
                        else: 
                            lastJob = lastJob + " " + job
                        
                print("Processing: " + str(processingDiary))        
                print(code + "|" + specialSection + "|" + str(lastDate) + "|" + str(lastOpCode) + "|" + job + "|" + str(lastRate) + "|" + str(lastUnit))
        pageNum+=1
    #if (page == 50):
    #    break;
print('done')
outfile.close()