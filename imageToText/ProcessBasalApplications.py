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
    print("test line for crops: " + line)
    for crop in crops:
        print("crop occ: " + crop + ", " + str(line.find(crop))) 
        lline = line.lower()
        lcrop = crop.lower()
        if lline.find(lcrop) >= 0 and lline.find(lcrop) <= 5: # look for the crop near the start of the line (first 5 chars)
        #if line.lower().startswith(crop.lower()):
            print("got crop : " + crop)
            cropSection = CropSection(crop,line[len(crop)+1:].strip())
            #cropSection.cropName(crop)
            #print("====>crop: " + crop)
            #print("====>line: " + cropSection.data)
            #cropSection.data()
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
                print("X")
            elif cropSection:
                print("Y")
                cropSection.data = " ".join([cropSection.data,line]) 
            else:
                print("Z")
                cropSection = CropSection("all crops",line)
    #print(cropSection.cropName + " - [" + cropSection.data + "]")
    cropSections.append(cropSection)
    return cropSections

def tidyApplicationData(data):
    ndata = data.replace("icide)","icide:").replace("killer)","killer:")
    return ndata

def loopDocs():
    year = ""
    fileList = os.listdir(srcdocs)
    fileList.sort()
    corrections = []
    sections = ["weedkiller:","fungicide:","insecticide:","manures:","weedkillers:"]
    
    with open("D:\\Work\\rothamsted-ecoinformatics\\YieldbookDatasetDrafts\\basalCorrections.csv", 'r') as infile:
        for line in infile:
            corrections.append(line.strip())
    
    for idx, fname in enumerate(fileList):
        nyear = fname[0:4]
        
        print("idx: " + str(idx) + ":  nyear = " + nyear + ", year =  " + year)
        if int(nyear) >= 1968 and int(nyear) <= 1991 and fname.endswith(".jpg"): 
            page = getPageScan(srcdocs + "\\" + fname)
            print("RAW PAGE:::::::::::::::::")
            print(page)
            print("\RAW PAGE:::::::::::::::::")
            
            #page = correctWords(page.replace("\n"," ").split(" "),corrections)
            page = page.replace("\n"," $$ $$ ") # This trick is for retaining line breaks, while allowing for testing line break joined words...
            page = correctWords(page.split(" "),corrections)
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
                #npage = ""
                if page.find("Basal applications") >-1:
                    cutStart = page.find("Basal applications")+19
                    print("a")
                    #npage = page[page.find("Basal applications")+19:] # this should stop everything before the Cultivations from being processed
                    #print(npage)
                elif page.find("Standard applications") >-1:
                    cutStart = page.find("Standard applications")+22
                    #npage = page[page.find("Standard applications")+22:]
                    print("b")
                    #print(npage)
                #fpage = npage
                if page.find("Cultivations, etc") > -1:
                    print("d")
                    cutEnd = page.find("Cultivations, etc")
                    #fpage = npage[:npage.find("Cultivations")]
                elif page.find("Seed") > -1:
                    cutEnd = page.find("Seed")
                    print("c")
                    #fpage = npage[:npage.find("Seed")]
                
                print(nyear + " : " + str(cutStart) + " : " + str(cutEnd) + " : " + str(len(page)))
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
                    
                    #print(data)
                
                    #section = ""
                    #for idx2, part in enumerate(applicationData):
                    #    sectionParts = part.split(" ")
                    #    lastWord = sectionParts[len(sectionParts)-1].strip()
                    #    print("(" + lastWord + ")")
                    #    oldSection = section
                    #    if lastWord in sections:
                        #if part[len(part)-1].lower() in sections:
                            #if len(prevLine) > 0:
                            #    outfile.write(str(nyear) + "|" + section + "|" + part) 
                            #    outfile.write("\n")
                    #        section = lastWord
                            #part = " ".join(sectionParts[:len(sectionParts)-2])
                    #    if len(section) > 0 and idx2 > 0:
                     #       part.replace(cropSection.cropName,"")
                      #      outfile.write("|".join([str(experiment),str(nyear),cropSection.cropName,oldSection,str(part)]))
                       #     outfile.write("\n")
                            
                    
                #outfile.write(str(nyear) + "|" + section + "|" + part) 
                #outfile.write("\n")
                #page = page.replace("\n"," ")
                #outfile.write(str(nyear) + ": " + page) 
                #outfile.write("\n")   

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
crops = config['EXPERIMENT']['crops'].split(",")
print(crops)
loopDocs()
#loopDocs("D:\\work\\yieldbooks\\Exhaustion\\")