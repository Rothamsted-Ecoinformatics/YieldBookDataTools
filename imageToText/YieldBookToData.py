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


def enhance(fname):
    img = cv2.imread(fname)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    #img = cv2.medianBlur(img,3)
    #img = cv2.bilateralFilter(img,7,150,150)
    #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    #filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
    kernel = np.ones((1, 1), np.uint8)
    #opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    #closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    #img = cv2.bitwise_or(img, closing)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ##img = cv2.bilateralFilter(img,9,70,70)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    ##img = cv2.GaussianBlur(img, (1, 1), 0)
    img = cv2.fastNlMeansDenoising(img,None,7,21,10)
    #cv2.imwrite("D:\\code\\python\\workspace\\YieldBookDataTools\\test data\\2007\\out\\"+fname, img)
    return img

def getPageScan(pathToFile):
    img = enhance(pathToFile)
    scan = pytesseract.image_to_string(img, lang='lat+eng', config='--dpi 300 --psm 4',nice=0,output_type=Output.DICT)
    page = scan.get("text")
    return page    

# Note replicated experiments will be listed together and therefore have two codes listed. convert these to comma delimited
def getCode(page):
    p = re.compile("[0-9]{2}\/[A-Z]\/[A-Z]{2}\/[0-9]{1,3}")
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
    
def getJobDate(job):
    p = re.compile("[0-9]{1,2}-[\w]+-[0-9]{2}") # Could extend this to have different date formats
    dateMatch = p.search(job)
    date = None
    if (dateMatch):
        date = dateMatch.group(0)
        job = job[dateMatch.end():].strip()
    return date, job

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