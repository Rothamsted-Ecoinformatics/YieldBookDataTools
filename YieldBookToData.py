'''
Created on 29 Nov 2018

Earliest format has experimental diary as free text. Other metadata more sparse

@author: ostlerr
'''
#import cv2
import numpy as np
#import pytesseract
import re
#from pytesseract.pytesseract import Output
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import string

corrections = []
with open("D:\\Work\\rothamsted-ecoinformatics\\YieldbookDatasetDrafts\\corrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())

months = ("Jan", "Feb", "Mar", "Apr", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec", "Mey") # Note Mey as seems to be a problem catching correction

# # def enhance(fname):
# #     img = cv2.imread(fname)
# #     img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
# #     img = cv2.medianBlur(img,3)
# #     #img = cv2.bilateralFilter(img,3,100,100)
    
# #     #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
# #     #filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
# #     kernel = np.ones((1, 1), np.uint8)
# #     img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# #     img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# #     #img = cv2.bitwise_or(img, closing)
# #     #kernel = np.ones((1, 1), np.uint8)
# #     #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #     #img = cv2.bilateralFilter(img,1,5,5)
# #     #img = cv2.dilate(img, kernel, iterations=1)
# #     #img = cv2.erode(img, kernel, iterations=1)
# #     #name = fname.split("\\")[7]
    
# #     #name2 = name.split(".")[0]
# #     #print("name2: " +name2)
# #     #cv2.imwrite("D:\\Code\\python\\workspace\\YieldBookDataTools\\" + name2 + ".png", img)
# #     #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# #     #cv2.imwrite("D:\\Code\\python\\workspace\\YieldBookDataTools\\" + name2 + "_2.png", img)
# #     ##img = cv2.GaussianBlur(img, (1, 1), 0)
# #     #img = cv2.fastNlMeansDenoising(img,None,7,21,150)
    
# #     return img

# Looks for any 4 character word and if it has at least 3 numbers assumes it is a number
def looksLikeYear(word):
    nword = removePunctuation(word,["&","%","}"])
    if (len(nword) == 4): 
        numCount= 0
        for c in nword:
            if c.isdigit():
                numCount += 1
        if numCount >= 3 or (numCount == 2 and nword[0:2] == "19"):
            return True
    return False 

def isStop(line):
    lline = line.lower()
    for stopper in ['grain tonnes/hecatare','table of means','summary of results','standard error','broadbalk wilderness']: #sectionStops:
        if lline.startswith(stopper) or fuzz.ratio(lline,stopper) > 80:
            return True
    return False

def startCultivations(line):
    lline = line.lower()
    lline = lline.translate(str.maketrans({a:None for a in string.punctuation}))
    if lline.startswith("cultivations"):
        return True
    return False

def startsWithSection(line, sectionNames):
    lline = removePunctuation(line.lower(),[])
    for name in sectionNames:
        if lline.startswith(name): # or fuzz.token_set_ratio(name,lline) > 80:
            return name, line[len(name):]    
    return None,line

#this is redundant... rework for leys ...check then go to end of line
def checkForSection(line, sectionNames):
    lline = removePunctuation(line.lower(),[])
    for name in sectionNames:
        if lline.startswith(name):
            return True, lline#name
    return False, None

def formatDate(day,month,year):
    if day in months: # check day and months right way around and if not swap.
        tday = day
        day = month
        month = tday
    d = "-".join([day,month,year])
    return d, month

def removePunctuation(value, exclusions):
    result = ""
    for c in value:
        if c in exclusions or c not in string.punctuation:
            result += c
    return result

# Note replicated experiments will be listed together and therefore have two codes listed. convert these to comma delimited
def getCode(content):
    p = re.compile(r"[0-9]{2}\/[A-Z]\/[A-Z]{1,2}\/[0-9]{1,3}")
    codeList = p.findall(content)
    codes = ",".join(map(str,codeList))
    return codes

def getOperationCode(job):
    codeMatch = re.search(r".?[apfs].? ", job)
    code = None
    if(codeMatch):
        r= re.compile(r"[^apfs]") # this should strip down to just the character
        code = r.sub("",codeMatch.group(0))
        job = job[codeMatch.end():].strip()
    return code, job
    
def checkJobDate(line):
    p = re.compile(r"[0-9]{1,2}-[\w]+-[0-9]{2}") # Could extend this to have different date formats
    dateMatch = p.search(line)
    date = None
    isDate = False
    if (dateMatch):
        date = dateMatch.group(0)
        line = line[dateMatch.end():].strip()
        isDate = True
    return isDate, date, line

def getRateUnitsJob(job):
    rateMatch = re.search(r"[0-9]{1,3}\.[0-9]{2}", job)
    rate = None
    units= None
    if (rateMatch):
        rate = rateMatch.group(0)
        units = job[rateMatch.end():].strip()
        job =job[:rateMatch.start()].strip()
    return rate, units, job

def clearSpace(matchObject):
    return matchObject.group(0).replace(" ", "")

def removeBlankLines(content):
    lines = content.split("\n")
    lines = list(filter(None,lines))
    return "\n".join(lines)

# Note there is a bias based on word length = e.g. 3 letter word gives score 67 if just one change. Should also ignore 2 letter words
def correctWords(content):
    words = content.split(" ") # chunk everything into words
    newWords = []
    for word in words:
        # some special force replacements 
        word = word.replace("0ct","Oct").replace("Mey","May")
        mword = ""
        lastChar = ""
        firstChar = ""
        hasPunc = False
        hasPrePunc = False
        if len(word) > 2:
            word = word.strip().replace(":","")
            
            lastChar = word[len(word)-1]
            if lastChar in string.punctuation:
                word = word[:len(word)-1]
                hasPunc = True
            
            firstChar = word[0]
            if firstChar in ["(","'"]:
                if word[1] == "'":
                    firstChar += "'"
                    word = word[1:]
                else:
                    word = word[2:]
                hasPrePunc = True
            
            wordLen = len(word)
            cutOff=70
            if wordLen == 3:
                cutOff = 65
            elif (wordLen == 4):
                cutOff = 74
                
            #matched = process.extractBests(word,corrections,scorer=fuzz.ratio,score_cutoff=cutOff)
            #print(matched)
            matched = process.extractOne(word,corrections,scorer=fuzz.ratio,score_cutoff=cutOff)
            if matched and wordLen > 2:
                mword = matched[0]
            else:
                mword = word
        else: 
            mword = word
        
        if hasPunc:
            mword += lastChar

        if hasPrePunc:
            mword = firstChar + mword
        newWords.append(mword)
    return newWords