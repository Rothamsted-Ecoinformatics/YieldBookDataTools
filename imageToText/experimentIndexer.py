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
        
class Experiment:
    def __init__(self):
        self.hasCode = False
        self.code = None
        self.title = None
        self.source = None
    
    def __str__(self):
        return ": ".join([str(self.code),str(self.title),str(self.source)])

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
    groups = ("TURNIP RAPE","WINTER BEANS","SPRING LUPINS","SPRING BARLEY", "WINTER LUPINS", "WINTER LINSEED","WINTER BARLEY","NAVY BEANS","LINSEED","BROCCOLI","WINTER OILSEED RAPE","CABBAGES","SPRING WHEAT","BROAD BEANS","BEANS","SPRING OILSEED RAPE","FIELD BEANS","OILSEED RAPE","PHASEOLUS","POTATOES","WINTER WHEAT","FENUGREEK","SPRING OATS","SUNFLOWERS","PEAS","OATS","GRASS","MAIZE","SWEET CORN","MIXED CROP","BRUSSEL SPROUTS","KALE","MIXED CROPS","SUGAR BEET","SWEDES","LUPINS","ONIONS","BARLEY")
    
    
    
    matched = process.extractOne(line,groups,scorer=fuzz.ratio,score_cutoff=85)
    cg = CropGroup()
    #print(matched)
    if matched and len(line.split(" ")) <=3:
        cg.isGroup = True
        cg.groupName = str(matched[0])
    #print("done testing for group") 
    return cg

def isExperiment(line):
    experimentFirstWords = ("Broadbalk","Hoos","Wheat", "Exhaustion", "Garden","Hoosfield","Agdell","Barnfield","Park","Stackyard", "Saxmundham", "Woburn", "Rothamsted")
    words = line.split(" ")
    return True if words[0] in experimentFirstWords else False

def getSiteFromLine(line):
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

def getSiteFromCode(code):
    sites = []
    sitePart = (code.split("/",1))[0]
    if sitePart == "R" or sitePart == "G":
        sites.append("Rothamsted")
    elif sitePart == "W":
        sites.append("Woburn")
    elif sitePart == "S":
        sites.append("Saxmundham")
    elif sitePart == "BB":
        sites.append("Brooms Barn")
    elif sitePart == "R&W":
        sites.append("Rothamsted")
        sites.append("Woburn")
    else:
        sites.append("Undetermined")
    
    return sites    
    
def stripPunctuation(line):
    cleanLine = re.sub(r"[|,.:!;^='~?]","",line)
    cleanLine = re.sub(r" +"," ",cleanLine)
    return cleanLine

def processOldFormatExperiment(line):    
    codeMatch = re.search(r"(.{1,2}/.{1,2})", line)
    exp = Experiment()
    exp.source = line
    if(codeMatch):
        exp.code = re.sub(r" +","",codeMatch.group(0))
        exp.title = line[:codeMatch.start()].strip()
        exp.hasCode = True
         
    return exp

def hasNewExperimentCode(line):
    return re.search(r"([\w&]{1,3}[ ]?/[ \w]{1,3}/[ \w]{,4})", line.upper())

def processNewFormatExperiment(line):
    codeMatch = hasNewExperimentCode(line)
    exp = Experiment()
    exp.source = line
    if(codeMatch):
        exp.code = re.sub(r" +","",codeMatch.group(0))
        exp.title = line[:codeMatch.start()].strip()
        exp.hasCode = True
    return exp
    
year = None
rootDir = "D:\\Code\\python\\workspace\\YieldBookDataTools\\test data\\pages"
corrections = ("fumigants","Stackyard","Ryegrass","Potatoes","Aldicarb","weevils","insecticides","control","Dwarf","varietal","sparying","dates","Sugar","sowing","Mangolds","growth","Krilium","placement","varieties","inoculation","phosphate","Gangrene","levels","rape","Barnfield","Stackyard","Hoosfield","Broadbalk","Garden","spring","arable","Old","application","Index","paraquat","spacing","Decline","Cultivation","Saxmundham","grass","Manuring","haulm","Decline","Take-all","Chemical","Exhaustion","Weedkiller","Concentrated","Straw","Trefoil","land","drilling","aphids","residual","Strips","Winter","beans","Methods","Barley","Eyespot","Woburn","wireworm","seeds","Rothamsted","Experiments","Wheat","Long","3-Course","4-Course","6-Course","Rotation","Rotations", "Miscellaneous","and")
fileList = os.listdir(rootDir)
expGroupName = None
cropGroupName= None
prevLine = None
foExperiments = open("D:\\work\\Rothamsted-Ecoinformatics\\Lists\\experiments.csv", "a+")
for fname in fileList:
    iyear = int(fname[9:13])
    cropGroupName = None # force reset this for each page
    if iyear > 1968:
        page = getPageScan(rootDir + "\\" + fname)
        print("+++++++++++++++++PAGE+++++++++++++++++++++")
        print (page)
        print("+++++++++++++++++/PAGE+++++++++++++++++++++")
        rawlines = page.split("\n")
        
        lines = list(filter(None,rawlines))
        nofLines = len(lines)
        for idx, line in enumerate(lines):
            cleanedLine = stripPunctuation(line)
            correctedLine = correctLine(cleanedLine, corrections)
            print("orignal  : " + line)
            print("corrected: " + correctedLine)
            expGroup = testForExperimentGroup(correctedLine)
            cropGroup = testForCropGroup(correctedLine)
            #code = getCode(correctedLine)
            
            if expGroup.isGroup: # new group
                expGroupName = expGroup.groupName
                expGroup.isGroup = False
                cropGroup = None
                print("expGroupName: " + expGroupName)
            elif iyear >=1969 and cropGroup.isGroup and expGroupName in ["Annuals", "Annual Experiments"]: # new crop 
                cropGroupName = cropGroup.groupName
                cropGroup.isGroup = False
                print("crops")
            else:
                print("hello 1")
                if iyear < 1965 and expGroupName in ["Classicals","Classical Experiments"]:
                    print("hello 2")
                    nextLine = lines[idx+1]
                    if not isExperiment(nextLine) and not expGroup.isGroup:
                        correctedLine = " ".join([correctedLine,correctLine(nextLine, corrections)])
                        idx+=1
                    sites = getSiteFromLine(correctedLine)
                    for site in sites:
                        foExperiments.write("|".join([str(iyear),site,expGroupName,correctedLine," "]))
                        foExperiments.write("\n")    
                elif re.split(r"[/]",correctedLine) or isExperiment(correctedLine):
                    print("hello 3")
                    if iyear >= 1969: 
                        experiment = processNewFormatExperiment(correctedLine)
                    else:
                        experiment = processOldFormatExperiment(correctedLine)
                    print(experiment)
                    if experiment.hasCode:
                        correctedLine = experiment.title
                        if iyear >= 1990: #This is when double lines swap code line order (code is now first line instead of last line0 
                            
                            tempIdx = idx+1
                            if tempIdx < nofLines:
                                nextLine = lines[tempIdx]
                                ok = True
                                nextEg = testForExperimentGroup(nextLine)
                                nextCg = testForCropGroup(nextLine)
                                while ok and not isExperiment(nextLine) and not hasNewExperimentCode(nextLine) and not nextCg.isGroup and not nextEg.isGroup:
                                    correctedLine = " ".join([correctedLine,nextLine])
                                    print(correctedLine + " : " + str(tempIdx) + " : " + str(nofLines))
                                    tempIdx+=1
                                    if tempIdx >= nofLines:
                                        ok=False
                                        nextLine = ""
                                    else:
                                        nextLine = correctLine(lines[tempIdx],corrections)
                                        idx = tempIdx
                                
                        if prevLine:
                            correctedLine = " ".join([prevLine,correctedLine])
                            prevLine = None
                        if cropGroupName:
                            print("crop name: " + str(cropGroupName))
                            correctedLine = ": ".join([cropGroupName,correctedLine])
                        if iyear >= 1969:
                            sites = getSiteFromCode(experiment.code)
                        else:
                            sites = getSiteFromLine(correctedLine) 
                        for site in sites:
                            foExperiments.write("|".join([str(iyear),site,expGroupName,correctedLine,experiment.code]))
                            foExperiments.write("\n")
                    else: #a line
                        print("hello 4")
                        prevLine = correctedLine
                else: #a line
                    print("hello 5")
                    prevLine = correctedLine
foExperiments.close()        
print('done')