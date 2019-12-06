'''
Created on 29 Nov 2018

Earliest format has experimental diary as free text. Other metadata more sparse

@author: ostlerr
'''
import cv2
import numpy as np
import pytesseract
import re
from pytesseract.pytesseract import Output
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import string

months = ("Jan", "Feb", "Mar", "Apr", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec", "Mey") # Note Mey as seems to be a problem catching correction

corrections = []
with open("D:\\Work\\rothamsted-ecoinformatics\\YieldbookDatasetDrafts\\corrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())
        
def enhance(fname):
    img = cv2.imread(fname)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img = cv2.medianBlur(img,3)
    #img = cv2.bilateralFilter(img,3,100,100)
    
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    #filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    #img = cv2.bitwise_or(img, closing)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.bilateralFilter(img,1,5,5)
    #img = cv2.dilate(img, kernel, iterations=1)
    #img = cv2.erode(img, kernel, iterations=1)
    #name = fname.split("\\")[7]
    
    #name2 = name.split(".")[0]
    #print("name2: " +name2)
    #cv2.imwrite("D:\\Code\\python\\workspace\\YieldBookDataTools\\" + name2 + ".png", img)
    #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #cv2.imwrite("D:\\Code\\python\\workspace\\YieldBookDataTools\\" + name2 + "_2.png", img)
    ##img = cv2.GaussianBlur(img, (1, 1), 0)
    #img = cv2.fastNlMeansDenoising(img,None,7,21,150)
    
    return img

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
    #lline = lline.translate(str.maketrans({a:None for a in string.punctuation}))
    print("test section start  -:- " + lline)
    for name in sectionNames:
        if lline.startswith(name): # or fuzz.token_set_ratio(name,lline) > 80:
            print("section is: " + name)
            return name, line[len(name):]
    return None,line

#this is redundant... rework for leys ...check then go to end of line
def checkForSection(line, sectionNames):
    lline = removePunctuation(line.lower(),[])
    print("test section start  -:- " + lline)
    #if len(sectionNames) > 0:
    for name in sectionNames:
        if lline.startswith(name):
            print("a: " + lline)
            return True, lline#name
    return False, None

def formatDate(day,month,year):
    if day in months: # check day and months right way around and if not swap.
        tday = day
        day = month
        month = tday
    d = "-".join([day,month,year])
    #d = ""
    #if month in ["Sept","Oct","Nov","Dec"]:
    #    d = "-".join([day,month,str(int(year)-1)])
   # else:
    #    d = "-".join([day,month,year])
    return d, month

def removePunctuation(value, exclusions):
    result = ""
    for c in value:
        if c in exclusions or c not in string.punctuation:
            result += c
    return result

def getPageScan(pathToFile):
    img = enhance(pathToFile) # use --psm 6 for normal use lat/eng
    scan = pytesseract.image_to_string(img, lang='eng', config='--dpi 300 --psm 6',nice=0,output_type=Output.DICT)
    #scan = pytesseract.image_to_pdf_or_hocr(img, lang='eng', config='--dpi 300 --psm 6',nice=0,extension='hocr')
    page = scan.get("text")
    return page    

# Note replicated experiments will be listed together and therefore have two codes listed. convert these to comma delimited
def getCode(page):
    p = re.compile(r"[0-9]{2}\/[A-Z]\/[A-Z]{1,2}\/[0-9]{1,3}")
    codeList = p.findall(page)
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

def toCorrectedLines(page):
    # some special force replacements
    page = page.replace("LO gals","40 gals")
    page = re.sub(r"My ([\d]{1,2})",r"May \1",page)
    page = re.sub(r" ([\d]{1,2}) and ",r" \1, ",page) # for fixing date formats 
    lines = page.split("\n")
    lines = list(filter(None,lines))
    cleanLines = []
    for line in lines:
        line = re.sub(r'(\w)-(\w)',r'\1 - \2',line) # ensures dashes are surrounded by spaces
        rawwords = line.split(" ") # chunk everything into words
        corrected = correctWords(rawwords)
        cleanwords = corrected.split(" ")
        words = list(filter(None,cleanwords))
        cleanLine = " ".join(words)
        cleanLines.append(cleanLine)
    return cleanLines

def correctLine(line):
    correctedLine = correctWords(line.split())
    return correctedLine

# Note there is a bias based on word length = e.g. 3 letter word gives score 67 if just one change. Should also ignore 2 letter words
def correctWords(words):
    newWords = []
    for word in words:
        # some special force replacements 
        word = word.replace("0ct","Oct").replace("Mey","May")
        if len(word) > 2:
            word = word.strip()
            lastChar = ""
            hasPunc = False 
            
            lastChar = word[len(word)-1]
            if lastChar in string.punctuation:
                word = word[:len(word)-1]
                hasPunc = True
            
            wordLen = len(word)
            cutOff=70
            if wordLen == 3:
                cutOff = 65
            elif (wordLen == 4):
                cutOff = 74
                
            matched = process.extractBests(word,corrections,scorer=fuzz.ratio,score_cutoff=cutOff)
            #print(matched)
            matched = process.extractOne(word,corrections,scorer=fuzz.ratio,score_cutoff=cutOff)
            if matched and wordLen > 2:
                if hasPunc:
                    newWords.append(matched[0]+lastChar)
                else: 
                    newWords.append(matched[0])
            else:
                if hasPunc:
                    newWords.append(word+lastChar)
                else:
                    newWords.append(word)
        else: 
            newWords.append(word)        
    return " ".join(newWords)