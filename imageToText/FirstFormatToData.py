'''
Created on 3 Dec 2018

@author: ostlerr
'''
import cv2
import numpy as np
import pytesseract
import re
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
from docutils.nodes import paragraph, Part

def getExperimentCodeAndName(testString):
    expCode = None
    expName = None
    #paragraphs = testString
    paragraphs = testString.split("\n")
    paragraphs = list(filter(None,paragraphs))
    print(paragraphs)
    
    idx0 = paragraphs[0].strip()
    codeMatches = re.match("[0-9]{2}/[A-Za-z]{1,2}/[0-9]", idx0)
    if (codeMatches):
        expCode = codeMatches.group(0)
        expName = paragraphs[1].strip() + " " + paragraphs[2].strip()
    else:
        expName = paragraphs[0].strip() + " " + paragraphs[1].strip() 
        
    print(str(expCode) + " - " + str(expName))   
    return expCode, expName
#     m = re.match("{1,2}/.{1,2}/.1{}\.?", testString, flags=0) #Looks for the experiment code pattern
#     if (m != None):
#         thisEx = testString.split(".")[0] # removes the 'page' component of the experiment code
#         print(thisEx)
#         thisEx = thisEx.split(" ")[0] # removes anything else in case of no page component
#         print(thisEx)
#         thisEx = thisEx.split("\n")[0] # removes anything else in case of no page component
#         print(thisEx)
#     else:
#         thisEx = ""
#     return thisEx

#try:
pageNum = 1
outfile = open("yieldbook1952.txt", "w+", 1)
fileList = os.listdir("V:\\YieldBook1952")

fileList.sort()

curEx = None
curName = None
processingDiary = False
specialSection = None
year = "1952"
months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
for fname in fileList:
    if fname.endswith(".jpg"): 
        print("processing document " + fname)
        print("document is page " + str(pageNum))
        
        page = getPageScan("V:\\YieldBook1952\\" + fname)
        page = re.sub(" +"," ",page).strip()
        
        if page:
            thisEx, thisName = getExperimentCodeAndName(page) 
            if (thisEx != curEx):
                curEx = thisEx
                curName = thisName
                processingDiary = False
                specialSection = None
                
            if (page.find("Cultivations,") > -1 or processingDiary == True): # this page has cultivations content - we want to extract this
                # cultivations typically have an operation and date separated by a : and terminate by a .
                # remove all line breaks then split on .
                processingDiary = True
                page = page[page.find("Cultivations,")+19:] # this should stop everything before the Cultivations from being processed
                
                parts = page.split() # chunk everything into words
                
                curOp = None
                curDate = None
                expectDay = False
                treatments = []
                for part in parts:
                    part.strip()
                    if (part.lower().startswith("sum") or part.lower().startswith("note")):
                        processingDiary = False
                        break
                    
                    elif expectDay:
                        curDate = " ".join([str(curDate),str(part)])
                        treatments.add("|".join([str(curDate),str(curOp)]))
                        curOp = None
                        curDate = None
                        expectDay = False
                    elif part in months:
                        curDate = part # we have a date
                        expectDay = True
                    else:
                        curOp = " ".join([str(curOp),str(part)])   
                                
                print(treatments)
                            
#                         if(partsLen == 2):
#                             outfile.write(fname + "|" + str(curEx) + "|" + str(curName) + "|" + specialSection + "|" + year + "|" + parts[0].strip() + "|" + parts[1].strip())
#                             outfile.write("\n")
#                         elif(partsLen > 2):
#                             outfile.write(fname + "|" + str(curEx) + "|" + str(curName) + "|" + specialSection + "|" + year + "|" + " ".join(parts[0:partsLen-1]) + "|" + parts[partsLen-1].strip())
#                             outfile.write("\n")
            
        pageNum+=1
    #if (page == 50):
    #    break;
print('done')
outfile.close()