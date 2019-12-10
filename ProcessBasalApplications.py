'''
Created on 7 Feb 2019

@author: ostlerr

Used to extract Basal Applications sections from documents 1974 to 1991. These sections capture information on manures and pesticides applied
'''
import os
from YieldBookToData import correctWords, removeBlankLines
import configparser
import xmltodict
import re

class CropSection:
    def __init__(self,pcropName,pdata):
        self.cropName = pcropName
        self.data = pdata
        
def newCrop(line):
    for crop in crops:
        lline = line.lower()
        lcrop = crop.lower()
        if lline.find(lcrop) >= 0 and lline.find(lcrop) <= 5: # look for the crop near the start of the line (first 5 chars)
            cropSection = CropSection(crop,line[len(crop)+1:].strip())
            return cropSection
    return None

def processCropSections(content):
    dataLines = content.split("\n")
    cropSection = None
    cropSections = []
    for line in dataLines: # this should split up into crop sections. next step should process these into application sections
        line = line.strip()
        if (len(line) > 3): # skip empty lines
            newCropSection = newCrop(line)
            if newCropSection:
                if cropSection:
                    cropSections.append(cropSection)
                cropSection = newCropSection
            elif cropSection:
                cropSection.data = " ".join([cropSection.data,line]) 
            else:
                cropSection = CropSection("all crops",line)
    cropSections.append(cropSection)
    return cropSections

def writeApplication(cropSection, application, applicationText):
    allApplications = applicationText.split(". ")
    for singleApplication in allApplications:
        application.replace(":","")
        outfile.write("|".join([str(experiment),str(year),cropSection.cropName,application,singleApplication.strip()]))
        outfile.write("\n")

def tidyApplicationData(content):
    content = content.replace("icide)","icide:").replace("killer)","killer:")
    return content

def applyCorrections(content):
    # Note this preserves lines as they provide structural cues to help with processing
    # some special force replacements - these could be applied to the whole doc
    
    content = re.sub(" +"," ",content).strip()
    content = re.sub(r"(\d),(\d)",r"\1.\2",content) # decimals
    corrected = correctWords(content)
    words = list(filter(None,corrected))
    return " ".join(words)

def process(content):
    #content = applyCorrections(content)
    print (content)
    data = False
    if content.find("Basal applications") > -1 or content.find("Standard applications") > -1:
        cutStart = 0
        cutEnd = len(content)-1 
        data = True
        
        if content.find("Basal applications") >-1:
            cutStart = content.find("Basal applications")+19
        elif content.find("Standard applications") >-1:
            cutStart = content.find("Standard applications")+22
        
        if content.find("Seed") > -1:
            cutEnd = content.find("Seed")
        elif content.find("seed") > -1:
            cutEnd = content.find("seed")
        elif content.find("Cultivations, etc") > -1:
            cutEnd = content.find("Cultivations, etc")
        
            
        content = str(content)[cutStart:cutEnd]
        content = content.strip()
    if data:
        content = tidyApplicationData(content)
        cropSections = processCropSections(content)
        for cropSection in cropSections:
            rawwords = applyCorrections(cropSection.data).split(" ")
            application = ""
            applicationText = ""
            for word in rawwords:
                if word.lower() in sections:
                    if len(application) > 0:
                        writeApplication(cropSection, application, applicationText)
                    application = word
                    applicationText = ""
                else:
                    applicationText = " ".join([applicationText,word.strip()])
            writeApplication(cropSection, application, applicationText)

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['sa_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['srcdoc']
crops = config['EXPERIMENT']['crops'].split(",")
sections = ["weedkiller","fungicide","insecticide","manures","weedkillers"]

with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    year = rep["year"]    
    print("start processing year: " + str(year))
    content = rep["rawcontent"]
    content = removeBlankLines(content)
    process(content)