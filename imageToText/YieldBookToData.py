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

months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec", "Mey") # Note Mey as seems to be a problem catching correction

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

def formatDate(day,month,year):
    if day in months: # check day and moths right way around and if not swap.
        tday = day
        day = month
        month = tday
    d = ""
    if month in ["Sept","Oct","Nov","Dec"]:
        d = "-".join([day,month,str(int(year)-1)])
    else:
        d = "-".join([day,month,year])
    return d, month

def removePunctuation(value, exclusions):
    result = ""
    for c in value:
        if c in exclusions or c not in string.punctuation:
            result += c
    return result

def getPageScan(pathToFile):
    img = enhance(pathToFile)
    scan = pytesseract.image_to_string(img, lang='lat+eng', config='--dpi 300 --psm 6',nice=0,output_type=Output.DICT)
    page = scan.get("text")
    return page    

# Note replicated experiments will be listed together and therefore have two codes listed. convert these to comma delimited
def getCode(page):
    p = re.compile("[0-9]{2}\/[A-Z]\/[A-Z]{1,2}\/[0-9]{1,3}")
    codeList = p.findall(page)
    codes = ",".join(map(str,codeList))
    print(codes)
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
    p = re.compile("[0-9]{1,2}-[\w]+-[0-9]{2}") # Could extend this to have different date formats
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
        #print(rateMatch)
        #print(job)
        rate = rateMatch.group(0)
        units = job[rateMatch.end():].strip()
        job =job[:rateMatch.start()].strip()
    return rate, units, job

def clearSpace(matchObject):
    return matchObject.group(0).replace(" ", "")

def getSponsors(page):
    p = re.compile("((?:[A-Z]\. *)+(?:Ma?c[A-Z][a-z]+|[A-Z][a-z]+))")# need to factor in McG
    sponsorList = p.findall(page)
    for sp in sponsorList:
        print(sp)
    sponsors = ",".join(map(str,sponsorList))
    return sponsors

def correctLine(line,spellings):
    correctedLine = correctWords(line.split(),spellings)
    return correctedLine

# Note there is a bias based on word length = e.g. 3 letter word gives score 67 if just one change. Should also ignore 2 letter words
def correctWords(words,spellings):
    #cutoffs = {3:67, 4:75, 5:80}
    print(spellings)
    newWords = []
    for word in words:
        ## add test for len here - 1 char
        lastChar = ""
        hasPunc = False            
        if len(word) > 1:
            lastChar = word[len(word)-1]
            if lastChar in string.punctuation:
                #print(word + " : " + lastChar)
                word = word[:len(word)-1]
                hasPunc = True
        
        wordLen = len(word)
        #if wordLen <= 2 or word in exclusions:
        #    newWords.append(word)
        #else:
        cutOff=70
        if wordLen == 3:
            cutOff = 65
        elif (wordLen == 4):
            cutOff = 79
        #print(":" + word + ":")
        
        matched = process.extractOne(word,spellings,scorer=fuzz.ratio,score_cutoff=cutOff)
        #print(matched)
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
    return " ".join(newWords)