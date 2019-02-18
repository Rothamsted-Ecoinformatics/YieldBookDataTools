'''
Created on 18 Feb 2019

@author: ostlerr
'''
import re
import configparser
import os
from imageToText.YieldBookToData import getPageScan, correctWords

corrections = []
fields = []

with open("D:\\work\\Rothamsted-Ecoinformatics\\YieldbookDatasetDrafts\\metadataCorrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())
        
with open("D:\\work\\Rothamsted-Ecoinformatics\\YieldbookDatasetDrafts\\fields.csv", 'r') as infile:
    for line in infile:
        fields.append(line.strip())

class Metadata():
    def __init__(self):
        self.object = ""
        self.design = ""
        self.plots = ""
        self.field = ""
        self.treatments = ""
        
def getSponsors(page):
    p = re.compile("((?:[A-Z]\. *)+(?:Ma?c[A-Z][a-z]+|[A-Z][a-z]+))")# need to factor in McG
    sponsorList = p.findall(page)
    #sponsors = ",".join(map(str,sponsorList))
    #return sponsors
    return sponsorList

def trimPage(tpage,start,end):
    tpage = tpage[tpage.lower().find(start.lower())+len(start):] # this should stop everything before the Cultivations from being processed
    if tpage.lower().find(end.lower()) > -1:
        tpage = tpage[:tpage.lower().find(end.lower())]
    tpage = tpage.strip()
    return tpage

def identifyField(text):
    for field in fields:
        if text.find(field):
            return(field)
    return ""

def loopDocs():
    global year
    fileList = os.listdir(srcdocs)
    fileList.sort()
    for fname in fileList:
        nyear = fname[0:4]
        if int(nyear) >= 1992 and int(nyear) <= 2006 and fname.endswith(".jpg"): 
            rawPage = getPageScan(srcdocs + "\\" + fname)
            print("RAWPAGE: [" + rawPage + "]")
            #rawPage = rawPage.replace("\n"," ") # This trick is for retaining line breaks, while allowing for testing line break joined words...
            rawPage = correctWords(rawPage.split(" "),corrections)
            metadata = Metadata()
            
            if rawPage.find("Object:") > -1:
                page = rawPage
                page = trimPage(page,"Object:","Sponsors:")
                metadata.object = page.replace("\n"," ")
                print("OBJECT: [" + metadata.object + "]")
                metadata.field = identifyField(metadata.object) 
                print("FIELD: ["+ metadata.field + "]")
            if rawPage.find("Design:") > -1:
                page = rawPage
                page = trimPage(page,"Design:","Plot dimensions") 
                metadata.design = page.replace("\n"," ")
                print("DESIGN: [" + metadata.design + "]") 
            
            if rawPage.lower().find("plot dimensions:") > -1:
                page = rawPage
                page = trimPage(page,"Plot dimensions:","Treatments") 
                metadata.design = page.replace("\n"," ")
                print("DIMENSIONS: [" + metadata.design + "]")
            if rawPage.find("Treatments:") > -1:
                page = rawPage
                page = trimPage(page,"Treatments:","Experimental diary") 
                metadata.treatments = page.replace("\n","\ ") # markdown paragraph
                print("TREATMENTS: [" + metadata.treatments + "]")
                
            if rawPage.find("Sponsors:") > -1:# or page.find("$$Seed") > -1:
                page = rawPage
                #page = page.replace("$$", " ")
                page = trimPage(page,"Sponsors:","The") 
                page = page.replace("\n"," ")
                print(page)
                sponsors = getSponsors(page)
                for sponsor in sponsors:
                    sponsorOutfile.write(experiment + "|" + str(nyear) + "|" + sponsor) 
                    sponsorOutfile.write("\n")
            
config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
sponsorOutfile = open(config['EXPERIMENT']['sponsorfile'], "w+", 1)
metadataOutfile = open(config['EXPERIMENT']['metadatafile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
loopDocs()