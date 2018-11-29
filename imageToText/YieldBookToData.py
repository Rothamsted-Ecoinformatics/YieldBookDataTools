'''
Created on 29 Nov 2018

@author: ostlerr
'''
import cv2
import numpy as np
import pytesseract
import sys
import re
import os
from pytesseract.pytesseract import Output

def enhance(fname):
    img = cv2.imread(fname)
        
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.bilateralFilter(img,9,70,70)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    #img = cv2.GaussianBlur(img, (1, 1), 0)
    img = cv2.fastNlMeansDenoising(img,None,7,21,10)
    
    return img

def getExperimentCode(testString):
    m = re.match(".{1,2}/.{1,2}?/", testString, flags=0) #Looks for the experiment code pattern
    if (m != None):
        thisEx = testString.split(".")[0] # removes the 'page' component of the experiment code
        thisEx = thisEx.split(" ")[0] # removes anything else in case of no page component
    else:
        thisEx = ""
    return thisEx

#try:
page = 1
outfile = open("yieldbook1965.txt", "w+", 1)
fileList = os.listdir("D:\\work\\yieldbooks\\YieldBook1965\\FullSize")
sorted(fileList)
for fname in fileList:
    if fname.endswith(".jpg"): 
        print("processing document " + fname)
        print("document is page " + str(page))
        img = enhance("D:\\work\\yieldbooks\\YieldBook1965\\FullSize\\" + fname)

        scan = pytesseract.image_to_string(img, lang='eng', config='--dpi 300 --psm 4',nice=0,output_type=Output.DICT)
        
        print("***********")
        line = scan.get("text")
        #print(scan)
        print("***********")
        
        if line:
            curEx = getExperimentCode(line) 
            
            if (line.find("Cultivations,") > -1): # this page has cultivations content - we want to extract this
            # cultivations typically have an operation and date separated by a : and terminate by a .
            # remove all line breaks then split on .
                
                line = line[line.find("Cultivations,"):] # this should stop everything before the Cultivations from being processed
            
                line = " ".join(line.split())
                dirtyJobs = line.split(". ")
                specialSection = ""
                for job in dirtyJobs:
                    if (job.startswith("SUM") or job.startswith("NOTE")):
                        break
                    job.replace("\n"," ").strip()
                    parts = job.split(":")
                    print(parts)
                    if(parts and len(parts)>1):
                        partsLen = len(parts)
                        if (partsLen > 2):
                            for part in parts:
                                if(part.strip().isupper()):
                                    if (part != specialSection):
                                        specialSection = part.strip()
                                    idx = parts.index(part)
                                    parts = parts[:idx]
                                    partsLen = len(parts)
                            
                        if(partsLen == 2):
                            outfile.write(curEx + "|" + specialSection + "|" + parts[0].strip() + "|" + parts[1].strip())
                            outfile.write("\n")
                        elif(partsLen > 2):
                            outfile.write(curEx + "|" + specialSection + "|" + " ".join(parts[0:partsLen-1]) + "|" + parts[partsLen-1].strip())
                            outfile.write("\n")
                    #print(job)
            
            
            
            #for item in lines:
            #    print(item)
            #    print("----------")
                
                #look for a pattern of upper case which indicates a change in the cultivated thing 
            #    outfile.write(item.strip())
                
            #    outfile.write("\n")
        page+=1
    #if (page == 50):
    #    break;
print('done')
outfile.close()


#except:
    #print("Unexpected error:", sys.exc_info()[0])   