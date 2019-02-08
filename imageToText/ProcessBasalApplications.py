'''
Created on 7 Feb 2019

@author: ostlerr

Used to extract Basal Applications sections from documents 1974 to 1991. These sections capture information on manures and pesticides applied
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
import string

def loopDocs(dir):
    year = ""
    fileList = os.listdir(dir)
    fileList.sort()
    corrections = []
    sections = ["weedkiller","fungicide","insecticide","manures","weedkillers"]
    
    outfile = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\ExhaustionLandBasal.txt", "w+", 1)
    with open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\basalCorrections.csv", 'r') as infile:
        for line in infile:
            corrections.append(line.strip())
    
    for idx, fname in enumerate(fileList):
        nyear = fname[0:4]
        
        print("idx: " + str(idx) + ":  nyear = " + nyear + ", year =  " + year)
        if int(nyear) >= 1974 and int(nyear) <= 1991 and fname.endswith(".jpg"): 
            page = getPageScan(dir + "\\" + fname)
            page = correctWords(page.replace("\n"," ").split(" "),corrections)
            data = False
            if page.find("Basal applications") > -1:
                data = True
                page = page[page.find("Basal applications")+19:] # this should stop everything before the Cultivations from being processed
                if page.find("Seed") > -1:
                    page = page[:page.find("Seed")]
                elif page.find("Cultivations") > -1:
                    page = page[:page.find("Cultivations")]
                
            print(data)
            if data:
                pageParts = page.split(":")
                print(pageParts)
                section = ""
                for idx2, part in enumerate(pageParts):
                    sectionParts = part.split(" ")
                    lastWord = sectionParts[len(sectionParts)-1].strip()
                    print("(" + lastWord + ")")
                    oldSection = section
                    if lastWord in sections:
                    #if part[len(part)-1].lower() in sections:
                        #if len(prevLine) > 0:
                        #    outfile.write(str(nyear) + "|" + section + "|" + part) 
                        #    outfile.write("\n")
                        section = lastWord
                        #part = " ".join(sectionParts[:len(sectionParts)-2])
                    if len(section) > 0 and idx2 > 0:
                        outfile.write(str(nyear) + "|" + oldSection + "|" + part) 
                        outfile.write("\n")
                        
                    
                #outfile.write(str(nyear) + "|" + section + "|" + part) 
                #outfile.write("\n")
                #page = page.replace("\n"," ")
                #outfile.write(str(nyear) + ": " + page) 
                #outfile.write("\n")   

loopDocs("D:\\work\\yieldbooks\\Exhaustion\\")