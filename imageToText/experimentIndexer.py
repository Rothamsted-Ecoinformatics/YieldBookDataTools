'''
Created on 17 Dec 2018

@author: ostlerr
'''
import os
from imageToText.YieldBookToData import *
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class ExperimentGroup:
    def __init__(self):
        self.isGroup = False
        self.groupName = None
        
    
class CropGroup:
    def __init__(self):
        self.isGroup = False
        self.groupName = None

def testForExperimentGroup(line):
    # "Rotation Experiments", "Crop Sequence Experiments", "Annual Experiments" added in 1961,  "Long Term Experiments","Short Term Experiments" removed in 1961
    groups = ("Classical Experiments", "Long Term Experiments","Short Term Experiments", "Rotation Experiments", "Crop Sequence Experiments", "Annual Experiments", "Rotations", "Annuals", "Classicals", "Crop Sequences")
    matched = process.extractOne(line,groups,scorer=fuzz.token_set_ratio,score_cutoff=85)
    eg = ExperimentGroup()
    #print(matched)
    if matched:
        eg.isGroup = True
        eg.groupName = str(matched[0])
    #print("done testing for group") 
    return eg
def testForCropGroup(line):
    # These appear from 1969 for annual experiments
    groups = ("TURNIP RAPE","WINTER BEANS","SPRING LUPINS","SPRING BARLEY", "WINTER LUPINS", "WINTER LINSEED","WINTER BARLEY","LINSEED","BROCCOLI","WINTER OILSEED RAPE","CABBAGES","SPRING WHEAT","BARLEY","BROAD BEANS","BEANS","SPRING OILSEED RAPE","OILSEED RAPE","PHASEOLUS","POTATOES","WINTER WHEAT","FENUGREEK","SPRING OATS","SUNFLOWERS","PEAS","OATS","GRASS","MAIZE","SWEET CORN","MIXED CROP","BRUSSEL SPROUTS","KALE","MIXED CROPS","SUGAR BEET","SWEDES","NAVY BEANS","LUPINS","ONIONS","FIELD BEANS")
    matched = process.extractOne(line,groups,scorer=fuzz.token_set_ratio,score_cutoff=85)
    cg = CropGroup()
    #print(matched)
    if matched:
        cg.isGroup = True
        cg.groupName = str(matched[0])
    #print("done testing for group") 
    return cg

def isExperiment(line):
    experimentFirstWords = ("Broadbalk","Hoosfield","Agdell","Barnfield","Park","Stackyard", "Deep", "Ley", "Green","Market","Irrigation")
    words = line.split(" ")
    return True if words[0] in experimentFirstWords or re.search(r"[0-9]",words[0]) else False

def getSite(line):
    sites = []
    if re.search(r"Woburn",line):
        sites.append("Woburn")
    if re.search(r"Saxmundham",line):
        sites.append("Saxmundham")
    if re.search(r"Rothamsted",line):
        sites.append("Rothamsted")
    if len(sites) == 0:    
        sites.append("Rothamsted")
        
    print(sites)
    return sites

def getCode(line):
    p = re.compile(r"(.{1,2}/.{1})")
    code = p.findall(line)
    return code[0] if code else None

def stripPunctuation(line):
    cleanLine = re.sub(r"[|,.:!;^='~?]","",line)
    cleanLine = re.sub(r" +"," ",cleanLine)
    return cleanLine

year = None
rootDir = "D:\\Code\\python\\workspace\\YieldBookDataTools\\test data\\pages"
corrections = ("Ryegrass","Potatoes","Aldicarb","weevils","insecticides","control","Dwarf","varietal","sparying","dates","Sugar","sowing","Mangolds","growth","Krilium","placement","varieties","inoculation","phosphate","Gangrene","levels","rape","Barnfield","Stackyard","Hoosfield","Broadbalk","Garden","spring","arable","Old","application","Index","paraquat","spacing","Decline","Cultivation","Saxmundham","grass","Manuring","haulm","Decline","Take-all","Chemical","Exhaustion","Weedkiller","Concentrated","Straw","Trefoil","land","drilling","aphids","residual","Strips","Winter","beans","Methods","Barley","Eyespot","Woburn","wireworm","seeds","Rothamsted","Experiments","Wheat","Long","3-Course","4-Course","6-Course","Rotation","Rotations", "Miscellaneous","and")
fileList = os.listdir(rootDir)
expGroupName = None
cropGroupName= None
prevLine = None
foExperiments = open("D:\\work\\Rothamsted-Ecoinformatics\\Lists\\experiments.csv", "a+")
for fname in fileList:
    page = getPageScan(rootDir + "\\" + fname)
    iyear = int(fname[9:13])
    print("+++++++++++++++++PAGE+++++++++++++++++++++")
    print (page)
    print("+++++++++++++++++/PAGE+++++++++++++++++++++")
    rawlines = page.split("\n")
    
    lines = list(filter(None,rawlines))
    
    for idx, line in enumerate(lines):
        cleanedLine = stripPunctuation(line)
        correctedLine = correctLine(cleanedLine, corrections)
        #print("orignal  : " + line)
        #print("corrected: " + correctedLine)
        expGroup = testForExperimentGroup(correctedLine)
        cropGroup = testForCropGroup(correctedLine)
        #code = getCode(correctedLine)
        
        if correctedLine == "Miscellaneous Data": 
            break
        elif ("index" in correctedLine.lower()):
            print("skip: " + correctedLine)
        elif expGroup.isGroup:
            expGroupName = expGroup.groupName
            print("expGroupName: " + expGroupName)
        elif iyear >=1969 and cropGroup.isGroup:
            cropGroupName = cropGroup.groupName
        else:
            parts = re.split(r"[/]",line)
            print(parts)
            print(prevLine)
            if len(parts) > 1 or isExperiment(correctedLine): #new experiment
                if prevLine:
                    correctedLine = " ".join([prevLine,correctedLine])
                    prevLine = None
                if cropGroupName:
                    print("crop name: " + str(cropGroupName))
                    correctedLine = " ".join([cropGroupName,correctedLine])
                sites = getSite(correctedLine)
                
                #if sites:
                #cleanedLine = stripPunctuation(correctedLine)
                print(sites)
                print("year: " + str(iyear))
                print("group: " + expGroupName)
                print("line: " + correctedLine)
                for site in sites:
                    foExperiments.write("|".join([str(iyear),site,expGroupName,correctedLine]))
                    foExperiments.write("\n")
                
            elif len(parts) == 1: #a line
                prevLine = line
foExperiments.close()        
print('done')