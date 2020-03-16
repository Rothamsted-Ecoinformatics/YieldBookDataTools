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
    for stopper in ['grain tonnes/hecatare','grain tonnes /hecatare','table of means','summary of results','standard error','broadbalk wilderness','note']: #sectionStops:
        if lline.startswith(stopper) or fuzz.partial_ratio(lline,stopper) > 80:
            return True
    return False

def startCultivations(line):
    lline = line.lower()
    lline = lline.translate(str.maketrans({a:None for a in string.punctuation}))
    if lline.startswith("cultivations") or fuzz.partial_ratio(line,"cultivations etc") >= 75:
        return True
    return False

def startsWithSection(line):
    if line.startswith("##"):
        return True, line.replace("#","")
    else:
        return False, line
##def startsWithSection(line, sectionNames):
##    lline = removePunctuation(line.lower(),[])
##    for name in sectionNames:
##        if lline.startswith(name): # or fuzz.token_set_ratio(name,lline) > 80:
            #line = line.replace(":","")
##            return name, line[len(name):]    
##    return "",line

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
    p = re.compile(r"[0-9SOli]{1,2}[-~][\w]+[~-][0-9SOli]{2,3}") # Could extend this to have different date formats. S, O, l are common mis-types to check for. 2,3 check is for occassional mis-types
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

def filterPunctuation(rawword):
    if rawword in ["-","~","="]:
        return True
    elif rawword in string.punctuation or rawword == " ":
        return False
    else:        
        return True

def removeBlankLines(content):
    lines = content.split("\n")
    lines = list(filter(None,lines))
    return "\n".join(lines)

# Note there is a bias based on word length = e.g. 3 letter word gives score 67 if just one change. Should also ignore 2 letter words
def correctWords(content):
    content = content.replace("\n\n","\n") # this is for line preservation
    content = re.sub(" +"," ",content).strip()
    newWords = []
    lines = content.split("\n")
    for line in lines:
        words = line.split(" ") # chunk everything into words
        for word in words:
            # some special force replacements 
            word = word.replace("0ct","Oct").replace("Mey","May").replace("Aua","Aug").replace("et","at")
            mword = ""
            lastChar = ""
            firstChar = ""
            hasPunc = False
            hasPrePunc = False
            if len(word) > 2:
                #word = word.strip().replace(":","")
                
                lastChar = word[len(word)-1]
                if lastChar in string.punctuation:
                    word = word[:len(word)-1]
                    hasPunc = True
                
                firstChar = word[0]
                if firstChar in ["(","'"]:
                    if word[1] == "'":
                        firstChar += "'"
                        word = word[2:]
                    else:
                        word = word[1:]
                    hasPrePunc = True
                
                wordLen = len(word)
                cutOff=70
                if wordLen == 3:
                    cutOff = 65
                elif (wordLen == 4):
                    cutOff = 74
                    
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
            newWords.append(mword.strip())
            #print("mword: " + mword)
        newWords.append("$$$$")
    print(newWords)
    #newWords = np.where(newWords=="$$$$", "\n", newWords)
    #
    #print(words)
    content = " ".join(newWords)
    #print(content)
    content = content.replace("$$$$ ","\n").replace("$$$$","")
    #content = re.sub("^\s","",content)
    print("--------------------")
    print(content)
    print("--------------------")
    return content