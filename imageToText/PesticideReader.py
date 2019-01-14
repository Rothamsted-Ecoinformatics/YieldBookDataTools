'''
Created on 14 Jan 2019

@author: ostlerr
'''

import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
import string
import re

splitters = [" H ", " D "," F "," I "," AD "," M "," N "," GR "]

def printPesticide(pesticide):
    ofPesticides.write(str(year) + ", " + pesticide)
    ofPesticides.write("\n")

def printAlarms(line):
    
    ofAlarms.write(",".join([str(year),str(line)]))
    ofAlarms.write("\n")
ofPesticides = open("D:\\work\\Rothamsted-Ecoinformatics\\YieldbookDatasetDrafts\\Pesticides\\PesticidesList.txt", "w+", 1)
ofAlarms = open("D:\\work\\Rothamsted-Ecoinformatics\\YieldbookDatasetDrafts\\Pesticides\\PesticidesToCheck.txt", "w+", 1)


def hasSplitter(line):
    for splitter in splitters:
        if line.find(splitter) > 0:
            return splitter
    return None
    
year = 1992
page = getPageScan("D:\\work\\yieldbooks\\Pesticides\\1992a.jpg")
lines = page.split("\n")
lines = list(filter(None,lines))
alarms = []
pesticides = []
prevWasSplitter = False
inPesticides = False
firstPart = ""
pidx = 0
for idx, line in enumerate(lines):
    if line.find("TRADE") > -1:
        inPesticides = True
    elif inPesticides:
        splitter = hasSplitter(line)

        if splitter:
            parts = line.split(splitter)
            tn = " ".join([firstPart,parts[0]])
            pesticides.append(",".join([tn,str(parts[1]),splitter]))
            firstPart = ""
            
        else:
            if line[0].isupper():
                firstPart = line
            elif len(line.split(" ")) <=3:
                print (pidx)
                pesticides[pidx-1] = " ".join([pesticides[pidx-1],line])
            else:
                printAlarms(line)
        pidx+=1
for pesticide in pesticides:
    printPesticide(pesticide)
ofPesticides.close()
ofAlarms.close()
print("done")