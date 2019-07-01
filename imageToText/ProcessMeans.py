'''
Created on 18 Jun 2019

@author: ostlerr
'''
import os
from imageToText.YieldBookToData import getPageScan, correctWords, removePunctuation
import configparser
import re
from fuzzywuzzy import fuzz

class treatment:
    def __init__(self,factor,factorDesc,level,levelDesc):
        self.factor = factor
        self.factorDesc = factorDesc
        self.level = level
        self.levelDesc = levelDesc
        
        
def selectPagePart(page):
    cutStart = page.find("Treatments:")+11
    cutEnd = 0
    if page.find("Basal applications") >-1:
        cutEnd = page.find("Basal applications")
    elif page.find("Experimental Diary") >-1:
        cutEnd = page.find("Experimental Diary")
    print(str(cutStart) + " : " + str(cutEnd))
    part =  str(page)[cutStart:] if cutEnd == 0 else str(page)[cutStart:cutEnd]
    print(part)
    return part
 
def fuzzy_replace(str_a, str_b, orig_str):
    l = len(str_a.split()) # Length to read orig_str chunk by chunk
    print(str(str_a) + " : " + str(orig_str))
    splitted = orig_str.split()
    for i in range(len(splitted)-l+1):
        test = " ".join(splitted[i:i+l])
        if fuzz.token_sort_ratio(str_a, test,False) > 75: #Using fuzzwuzzy library to test ratio
            before = " ".join(splitted[:i])
            after = " ".join(splitted[i+1:])
            return before+" "+str_b+" "+after
    return orig_str
    
config = configparser.ConfigParser()
config.read('config.ini')
#experiment = config['EXPERIMENT']['name']
#outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']

fileList = os.listdir(srcdocs)
fileList.sort()
treatments = []
for fname in fileList:
    #nyear = fname[0:4]
    #npage = fname[4:6]
    #print (nyear + " - " + npage)
    print(srcdocs + "\\" + fname)
    
    if fname.endswith("061.jpg"):
        page = getPageScan(srcdocs + "\\" + fname)
        
        cutStart = 0
        cutEnd = len(page)-1 
        #data = True
        print(page)
        page = page.replace("\n"," $$ $$ ") # This trick is for retaining line breaks, while allowing for testing line break joined words...
        page = correctWords(page.split(" "))
        page = page.replace(" $$ $$ ","\n")
        
        
        
        if page.find("Treatments") >-1:
            page = selectPagePart(page)
            print(page)
            lines = page.split("\n")
            lines = list(filter(None, lines)) 
             
            pLevel = re.compile("^[^a-z]+(?=\s[A-Z][a-z])") # ignores any lower case word
            pFactor = re.compile("^[1-9]\.\s[^a-z]+(?=\s[A-Z][a-z])")
            lastDesc = ""
            
            trtCode = ""
            for idx, line in enumerate(lines):
                m = pFactor.match(line)
                if (m):
                    factor = m.group()
                    factorDesc = line[m.end():]
                    print("FACTOR: " + str(factor) + " : " + str(factorDesc))
                else:
                    m = pLevel.match(line)
                    if(m):
                        level = m.group()
                        levelDesc = line[m.end():]
                        treatments.append(treatment(factor,factorDesc,level,levelDesc))
                    else:
                        trt = treatments.pop()
                        trt.levelDesc = " ".join([trt.levelDesc,line])
                        treatments.append(trt)
            
            for t in treatments:
                print(t.factor+ "," +t.factorDesc+ "," +t.level+ "," +t.levelDesc)
        else:
            #print("treatments: " + treatments)
            if page.lower().find("tables of means") >-1:
                page = str(page)[page.lower().find("tables of means"):cutEnd]
                print(page)
            else:    
                
                lines = page.split("\n")
                lines = list(filter(None, lines))
                headings = lines[1]
                newheadings = ""
                
                print("headings: " + headings)
                for t in treatments:
                    print("code: " + str(t.code))
                    headings = fuzzy_replace(t.code, t.code, headings)
                print("proc: " + headings)    
                for tidx, t in enumerate(treatments):
                    if headings.find(t.code) > -1:
                        newheadings = t.code if tidx == 0 else ",".join([newheadings,t.code])
                    
                print(newheadings)
                data = lines[2]
                dataItems = data.split(" ")        
                data = ","+",".join(dataItems)
                print(data)