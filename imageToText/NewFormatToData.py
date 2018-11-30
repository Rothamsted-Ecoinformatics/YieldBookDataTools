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
        
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.bilateralFilter(img,9,70,70)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    #img = cv2.GaussianBlur(img, (1, 1), 0)
    img = cv2.fastNlMeansDenoising(img,None,7,21,10)
    
    return img

# Not all pages have the code so need memory of the previous one
def getExperimentCode(testString, prevEx):
    m = re.match(".{1,2}/.{1,2}?/", testString, flags=0) #Looks for the experiment code pattern
    if (m != None):
        thisEx = testString.split(".")[0] # removes the 'page' component of the experiment code
        #print(thisEx)
        thisEx = thisEx.split(" ")[0] # removes anything else in case of no page component
        #print(thisEx)
        thisEx = thisEx.split("\n")[0] # removes anything else in case of no page component
        #print(thisEx)
    else:
        thisEx = prevEx
    return thisEx

def getSponsors(line):
    if (line.find("Sponsors:") > -1):
        line = line[line.find("Sponsors:"):]
        paragraphs = line.split("\n\n")
        foSponsors.write(curEx+","+paragraphs[0].strip())
        foSponsors.write("\n")
        
def getTitleAndObject(line):        
    curEx = ""  
    if (line.find("Object:") > -1):
        paragraphs = line.split("\n")
        print(paragraphs)
        curEx = paragraphs[0].strip()
        title = paragraphs[1].strip()
        objective = ""
        design = "" 
        plots = ""
        sponsor = ""
        treatments = ""
        section = 0
        for p in paragraphs:
            if (p.startswith("Object")):
                section= 1
                objective = (p.split(":")[1]).replace("\n", " ")
            elif (p.startswith("Sponsor")):
                section= 2
                sponsor = (p.split(":")[1]).replace("\n", " ")
            elif (p.startswith("Design")):
                section= 3
                design = (p.split(":")[1]).replace("\n", " ")
            elif ((p.startswith("Areas") or p.startswith("Whole") or p.startswith("Plot")) and len(p.split(":"))==2):
                section= 4
                plots = (p.split(":")[1]).replace("\n", " ")
            elif (p.startswith("Treatments")):
                section= 5
                #do nothing
                treatments = ""
            else:
                if (section == 1):
                    objective = objective +" "+p.strip() 
                if (section == 2):
                    sponsor = sponsor +" "+p.strip()
                if (section == 3):
                    design = design +" "+p.strip()
                if (section == 4):
                    plots = plots +" "+p.strip()
                if (section == 5):
                    treatments = treatments +" "+p.strip()   
        foTitleAndObject.write(curEx+"|"+title+"|"+objective+"|"+sponsor+"|"+design+"|"+plots)
        foTitleAndObject.write("\n")
    return curEx
page = 1
outfile = open("yieldbook1994.txt", "w+", 1)
foSponsors = open("sponsors1994.txt", "w+", 1)
foTitleAndObject = open("titleAndObject1994.txt", "w+", 1)
fileList = os.listdir("D:\\code\\python\\workspace\\YieldBookDataTools\\test data\\1994\\FullSize")
sorted(fileList)
curEx="" # set default
for fname in fileList:
    
    if fname.endswith(".jpg"): 
        print("processing document " + fname)
        print("document is page " + str(page))
        img = enhance("D:\\code\\python\\workspace\\YieldBookDataTools\\test data\\1994\\FullSize\\" + fname)
        
        scan = pytesseract.image_to_string(img, lang='eng', config='--dpi 300 --psm 4',nice=0,output_type=Output.DICT)
        
        #print("***********")
        line = scan.get("text")
        #print(line)
        print("***********")
        
        if line:
            newEx = getTitleAndObject(line)
            print(newEx + " + " + curEx)
            if (newEx.strip() != curEx and newEx.find("/")>1):
                curEx = newEx
            print(newEx + " + " + curEx)#getSponsors(line)
            #curEx = getExperimentCode(line,curEx) 
            
            if (line.find("Experimental diary:") > -1): # this page has the experimental diary:
                # Special sections identified by 1 : occurrence. 
                
                line = line[line.find("Experimental diary:"):] # this should stop everything before the Cultivations from being processed
            
                #line = " ".join(line.split()).strip()
                line = line.replace(",\n",", ")
                dirtyJobs = line.split("\n")
                specialSection = ""
                sameDay = ""
                for job in dirtyJobs:
                    parts = job.strip().split(":")
                    #print(parts)
                    partsLen = len(parts)
                    if (partsLen == 2 and len(parts[0])>1): #special part
                        if parts[0] == "Experimental diary":
                            specialSelection = "All plots"
                        else:    
                            specialSection = parts[0]
                        
                    elif(partsLen == 3):
                        if (len(parts[0].strip())>0 and re.match("[0-9]",parts[0],flags=0)):
                            sameDay = parts[0].strip()
                        outfile.write(curEx + "|" + specialSection + "|" + parts[2].strip().replace("\n"," ") + "|" + sameDay + "|" + parts[1].strip())
                        outfile.write("\n")
            
        page+=1
    #if (page == 50):
    #    break;
print('done')
outfile.close()
foSponsors.close()
foTitleAndObject.close()