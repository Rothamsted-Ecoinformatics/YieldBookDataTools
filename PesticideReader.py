'''
Created on 14 Jan 2019

@author: ostlerr
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *

def printPesticide(year,pesticide):
    i = pesticide.strip()
    i = i.replace("\xab", "+")
    i = i.replace("\xa5", "F")
    i = i.replace("*", "%")
    i = i.replace("$", "%")
    pesticide = i
    #ofPesticides.write(", ".join([str(year),str(pesticide.tradename).strip(),str(pesticide.type).strip(),i]))
    ofPesticides.write(", ".join([str(year),pesticide]))
    ofPesticides.write("\n")
    
ofPesticides = open("D:\\work\\Rothamsted-Ecoinformatics\\YieldbookDatasetDrafts\\Pesticides\\PesticidesList.txt", "w+", 1)

inPesticides = False
firstPart = ""
fileList = os.listdir("D:\\work\\yieldbooks\\Pesticides")
pyear = ""
for fname in fileList:
    year = fname[0:4]
    inPesticides = True if year == pyear else False
    
    page = getPageScan("D:\\work\\yieldbooks\\Pesticides\\" + fname)
    lines = page.split("\n")
    lines = list(filter(None,lines))
    curline = ""
    for line in lines:
        if line.find("TRADE") > -1 or line.find("Trade Name") > -1:
            inPesticides = True
        elif inPesticides:
            if line[0].isupper():
                if curline != "":
                    printPesticide(year,curline)
                curline = line
            else:
                curline = " ".join([curline,line])
    pyear = year            
printPesticide(year,curline)
ofPesticides.close()
print("done")