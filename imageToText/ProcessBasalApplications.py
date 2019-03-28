'''
Created on 7 Feb 2019

@author: ostlerr

Used to extract Basal Applications sections from documents 1974 to 1991. These sections capture information on manures and pesticides applied
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
import string
import configparser

class CropSection:
    def __init__(self,pcropName,pdata):
        self.cropName = pcropName
        self.data = pdata
        
def newCrop(line):
    global crops
    for crop in crops:
        lline = line.lower()
        lcrop = crop.lower()
        if lline.find(lcrop) >= 0 and lline.find(lcrop) <= 5: # look for the crop near the start of the line (first 5 chars)
            cropSection = CropSection(crop,line[len(crop)+1:].strip())
            return cropSection
    return None

def processCropSections(page):
    dataLines = page.split("\n")
    cropSection = None
    cropSections = []
    for line in dataLines: # this should split up into crop sections. next step should process these into application sections
        line = line.strip()
        if (len(line) > 3): # skip empty lines
            newCropSection = newCrop(line)
            #print(line)
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

def tidyApplicationData(data):
    ndata = data.replace("icide)","icide:").replace("killer)","killer:")
    return ndata

def loopDocs():
    year = ""
    fileList = os.listdir(srcdocs)
    fileList.sort()
    sections = ["weedkiller:","fungicide:","insecticide:","manures:","weedkillers:"]
    
    for idx, fname in enumerate(fileList):
        nyear = fname[0:4]
        
        if int(nyear) >= 1968 and int(nyear) <= 1991 and fname.endswith(".jpg"): 
            page = getPageScan(srcdocs + "\\" + fname)
            print("RAW PAGE:::::::::::::::::")
            print(page)
            print("\RAW PAGE:::::::::::::::::")
            
            page = page.replace("\n"," $$ $$ ") # This trick is for retaining line breaks, while allowing for testing line break joined words...
            page = correctWords(page.split(" "))
            page = page.replace(" $$ $$ ","\n")
            print("CORRECTED PAGE:::::::::::::::::")
            print(page)
            print("\CORRECTED PAGE:::::::::::::::::")
            page = page.strip()
            data = False
            fpage = ""
            if page.find("Basal applications") > -1 or page.find("Standard applications") > -1:
                cutStart = 0
                cutEnd = len(page)-1 
                data = True
                
                if page.find("Basal applications") >-1:
                    cutStart = page.find("Basal applications")+19
                elif page.find("Standard applications") >-1:
                    cutStart = page.find("Standard applications")+22
                if page.find("Cultivations, etc") > -1:
                    cutEnd = page.find("Cultivations, etc")
                elif page.find("Seed") > -1:
                    cutEnd = page.find("Seed")
                
                fpage = str(page)[cutStart:cutEnd]
                fpage = fpage.strip()
            print("=====================DATA=========================")    
            print(page.find("Standard applications"))
            print(len(fpage))
            print(fpage)
            print("=====================/DATA=========================")
            if data:
                cropSections = processCropSections(fpage)
                for cropSection in cropSections:
                    applicationData = tidyApplicationData(cropSection.data).split(" ")
                    application = ""
                    applicationText = ""
                    for word in applicationData:
                        if word in sections:
                            if len(application) > 0:
                                outfile.write("|".join([str(experiment),str(nyear),cropSection.cropName,application,applicationText.strip()]))
                                outfile.write("\n")
                            application = word
                            applicationText = ""
                        else:
                            applicationText = " ".join([applicationText,word.strip()])
                    outfile.write("|".join([str(experiment),str(nyear),cropSection.cropName,application,applicationText.strip()]))
                    outfile.write("\n")

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
crops = config['EXPERIMENT']['crops'].split(",")
loopDocs()