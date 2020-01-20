'''
Created on 8 Feb 2019

@author: ostlerr
'''
import os
from YieldBookToData import correctWords, removePunctuation, startsWithSection
import configparser
import re
import xmltodict

def applyCorrections(content):
    # Note this preserves lines as they provide structural cues to help with processing
    # some special force replacements - these could be applied to the whole doc
    content = re.sub(" +"," ",content).strip()
    content = re.sub(r"(\d),(\d)",r"\1.\2",content) # decimals
    return correctWords(content)

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['seeds_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
crops = config['EXPERIMENT']['crops'].split(",")

with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    year = rep["year"]
    print(year)
    if int(year) >= 1968 and int(year) <= 1991: 
        content = rep["rawcontent"]
        data = False
        if content.find("Seed:") > -1:# or page.find("$$Seed") > -1:
            data = True
            content = content[content.find("Seed:")+5:] # this should stop everything before the Cultivations from being processed
            content = applyCorrections(content) # applying corrections before finding seed can cause problems. 
            if content.find("Cultivations") > -1:
                content = content[:content.find("Cultivations")]
            content = content.strip() 
        
        if data:
            cropList = {}
            cropText = ""
            cropName = ""
            lines = content.split("\n")
            for line in lines:
                newCrop, newLine = startsWithSection(line,crops) 
                
                if newCrop:
                    cropList[cropName] = cropText
                    cropText = "" #set up the new section text
                    cropName = newCrop
                    line = newLine
                if len(line) > 1:
                    line = line.strip()
                    cropText = " ".join([str(cropText),line])    
            cropList[cropName] = cropText
            for crop, text in cropList.items():
                if text:
                    outfile.write(experiment + "|" + str(year) + "|" + crop + "|" + text.strip()) 
                    outfile.write("\n")

            