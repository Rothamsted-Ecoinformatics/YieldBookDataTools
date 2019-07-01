'''
Created on 7 Feb 2019

@author: ostlerr

Used to extract Basal Applications sections from documents 1974 to 1991. These sections capture information on manures and pesticides applied
'''
import os
from imageToText.YieldBookToData import getPageScan, correctWords
import configparser

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

def processCropSections(page):
    dataLines = page.split("\n")
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

def tidyApplicationData(data):
    ndata = data.replace("icide)","icide:").replace("killer)","killer:")
    return ndata

def writeApplication(cropSection, application, applicationText):
    allApplications = applicationText.split(". ")
    for singleApplication in allApplications:
        outfile.write("|".join([str(experiment),str(year),cropSection.cropName,application,singleApplication.strip()]))
        outfile.write("\n")

def process(page):
    page = page.replace("\n"," $$ $$ ") # This trick is for retaining line breaks, while allowing for testing line break joined words...
    page = correctWords(page.split(" "))
    page = page.replace(" $$ $$ ","\n")
    
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
        elif page.find("seed") > -1:
            cutEnd = page.find("seed")
            
        fpage = str(page)[cutStart:cutEnd]
        fpage = fpage.strip()

    if data:
        cropSections = processCropSections(fpage)
        for cropSection in cropSections:
            #if (cropSection):
            print(cropSection.data)
            applicationData = tidyApplicationData(cropSection.data).split(" ")
            application = ""
            applicationText = ""
            for word in applicationData:
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
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
crops = config['EXPERIMENT']['crops'].split(",")
fileList = os.listdir(srcdocs)
fileList.sort()
sections = ["weedkiller:","fungicide:","insecticide:","manures:","weedkillers:"]
year = ""
page = ""
for fname in fileList:
    nyear = fname[0:4]
    
    if int(nyear) >= 1968 and int(nyear) <= 1991 and fname.endswith(".jpg"): 
        print(nyear)
        thisPage = getPageScan(srcdocs + "\\" + fname)
        print(year)
        if nyear != year:
            process(page)
            page = thisPage
            year = nyear
        else:
            page += thisPage
process(page)