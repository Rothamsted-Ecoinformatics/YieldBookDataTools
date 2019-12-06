'''
Created on 3 Dec 2018

@author: ostlerr
'''
import os
from pytesseract.pytesseract import Output
from YieldBookToData import *
import string
import configparser

def looksLikeDay(word):
    nword = removePunctuation(word,["&","%","}"])
    if (len(nword) == 2 or len(nword) == 1):
        if nword in (["1b"]): # common errors which should be ignored
            return False
        numCount = 0
        for c in nword:
            if c.isdigit():
                numCount += 1
        if numCount >= 1:
            return True
    return False

# this method is all about finding the end of a cultivations segment. If no end is found by the end of the page then carries through to the next page    
def getOperations(lines):
    global cultivationsSegment
    global inCultivations# must be false because starting a new year ?
    inCultivations = False
    for line in lines:
        print(startCultivations(line))
        if(inCultivations):
            if isStop(line):    
                inCultivations = False
                print("ex cultivations")
                break
            else:                
                cultivationsSegment.append(line)
        elif startCultivations(line):
        #elif(fuzz.token_set_ratio(line,"Cultivations etc") >= 75): 
            print("in cultivations")
            cultivationsSegment.clear()
            inCultivations = True
            parts = line.split(" ")
            if (len(parts) >2):
                line = " ".join(parts[2:])
                cultivationsSegment.append(line)
    
    processCultivations()
    
def writeJob(sname,opDate,op):
    sDate, eDate = cleanDate(opDate,year)
    outfile.write("|".join([experiment,year,str(sname),str(sDate),str(eDate),op]))
    outfile.write("\n")    

#this method is about subsectioning the cultivations then writing them             
def processCultivations():   #cultivationSections = cultivationsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    sectionName = ""
    subsections = {}
    subsectionText = ""

    for line in cultivationsSegment:
        print(line)
        newSection, newLine = startsWithSection(line,sectionNames) 
        if (newSection):
            if(sectionName): # add the old section name to the dictionary. Length check is for misidentifications - sub sections should be short
                subsections[sectionName] = subsectionText
            subsectionText = "" #set up the new section text
            sectionName = newSection
            line = newLine
        
        if (len(line) > 1):
            subsectionText = " ".join([str(subsectionText),line])
    if not sectionName:
        sectionName = "All plots"
    subsections[sectionName] = subsectionText           # got a new section...probably
    
    # Now process the subsections:
    processSections(subsections)

def filterPunctuation(rawword):
    if rawword in ["-","~","="]:
        return True
    elif rawword in string.punctuation or rawword == " ":
        return False
    else:        
        return True
            
def processSections(subsections):
    for sname, stext in subsections.items():
        rawwords = stext.split()
        words = list(filter(filterPunctuation,rawwords))
        wordCount = len(words)
        opDate = ""
        curOp = ""
        prevOp = ""
        opCount=0
        idx = 0
        backupOp = ""
        while idx < wordCount:
            word = words[idx]
            
            cleanWord = removePunctuation(word,["-","~", "="]) 
            trimCount = 0
            if cleanWord in months:                
                # check prev
                fd = words[idx-3]
                dash = words[idx-2]
                ld = words[idx-1]
                if looksLikeDay(ld):
                    if looksLikeDay(fd) and dash in ["-", "~","="]:
                        opDate = "-".join([fd,ld])
                        trimCount = 2 #? 
                    else:
                        opDate = ld
                        trimCount = 1
                    opDate = " ".join([opDate,cleanWord])
                    year = ""
                    base = 0
                    if idx+1 < wordCount and looksLikeYear(words[idx+1]):
                        year = removePunctuation(words[idx+1],[]) 
                        opDate = " ".join([opDate,year])
                        base = 1
                    
                    if idx+(3+base) < wordCount and words[idx+(1+base)] in ["-","~","="] and looksLikeDay(words[idx+2]) and removePunctuation(words[idx+(3+base)],[]) in months:
                        opDate = " ".join([opDate," - ", str(words[idx+(2+base)]), str(removePunctuation(words[idx+(3+base)],[]))])
                        base +=3
                    idx = idx+base
                    if opCount == 0:
                        flashCurOp = curOp.split(" ")
                        opPart = flashCurOp[:len(flashCurOp)-trimCount]
                        curOp = " ".join(opPart)
                        curOp = curOp.replace(":", "").strip()
                        if(len(curOp) <= 2):
                            curOp = backupOp
                        if curOp == "and":
                            curOp = backupOp
                        opCount = 1
                    writeJob(sname,opDate,curOp)
                    opDate = None
                else:
                    curOp = " ".join([curOp,word])
            elif opCount == 1 and looksLikeDay(cleanWord) or looksLikeYear(word) or word in ["-", "~", "="]:
                pass
            else:
                if opCount == 1:
                    backupOp = curOp
                    curOp = word
                else: 
                    curOp = " ".join([curOp,word])
                opCount = 0
                    
            idx+=1    
        if opDate:
            if curOp == "and":
                curOp = backupOp
            writeJob(sname,opDate,curOp,experiment)
            #prevOp = curOp
     
def cleanDate(dirtyDate, year):
    global lyear
    sDate = ""
    eDate = ""

    if dirtyDate:
        dirtyDate = dirtyDate.replace("=","-").replace("—","-")
        dirtyDate = removePunctuation(str(dirtyDate), ("-"))
        dirtyDate = dirtyDate.replace(" and ",", ")
        dirtyDate = re.sub(r"(\d)-(\d)",r"\1 - \2",dirtyDate)
        print("dirtyDate: " + str(dirtyDate))

        parts = dirtyDate.split(" ")
        if re.match(r"\d{1,2} \w{3,5} - \d{1,2} \w{3,5} \d{4}",str(dirtyDate)):
            lyear = parts[5]
            sDate = "-".join([parts[0],parts[1],lyear])
            eDate = "-".join([parts[3],parts[4],lyear])
        elif re.match(r"\d{1,2} - \d{1,2} \w{3,5} \d{4}",str(dirtyDate)):
            lyear = parts[4]
            month = parts[3]
            sDate = "-".join([parts[0],month,lyear])
            eDate = "-".join([parts[2],month,lyear])
        elif re.match(r"\d{1,2} - \d{1,2} \w{3,5}",str(dirtyDate)):
            month = parts[3]
            sDate = "-".join([parts[0],month,lyear])
            eDate = "-".join([parts[2],month,lyear])
        elif re.match(r"\d{1,2} \w{3,5} \d{1,4}",str(dirtyDate)):
            lyear = parts[2]
            month = parts[1]
            sDate = "-".join([parts[0],month,lyear])        
        elif re.match(r"\d{1,2} \w{3,5}",str(dirtyDate)):
            if lyear == "":
                lyear = str(int(year)-1)
            month = parts[1]
            if (lyear == "" or lyear == str(int(year)-1)) and month in ("Jan","Feb","Mar","April","Apr","May","June","July"):
                lyear = year
            elif lyear == "":
                lyear = str(int(year)-1)

            sDate = "-".join([parts[0],month,lyear])
        else:
            sDate = "UNKNOWN"
            eDate = dirtyDate
            
    return sDate,eDate


    # dirtyDate = removePunctuation(str(dirtyDate), ("-"))
    # sDate = ""
    # eDate = ""
    # lyear = year # the local year from the date, rather than the doc
    # dates = dirtyDate.split("-")
    # if len(dates) > 0: # just one date
    #     sparts = dates[0].strip().split(" ")
    #     mnth = ""
    #     if len(sparts) == 2:
    #         sDate, mnth = formatDate(sparts[1],sparts[0],lyear)
    #     elif len(sparts) == 3:
    #         lyear = sparts[2]
    #         sDate, mnth = formatDate(sparts[1],sparts[0],lyear)            
    #     else:
    #         sDate = dirtyDate
    #     if len(dates) == 2:    
    #         eparts = dates[1].strip().split(" ")
    #         if len(eparts) == 1:
    #             eDate,month = formatDate(eparts[0],mnth,lyear)
    #         elif eparts[0] in months:
    #             eDate,month = formatDate(eparts[1],eparts[0],lyear)
    #         else:
    #             eDate,month = formatDate(eparts[0],mnth,lyear)
    # return sDate,eDate


config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
strSections = config['EXPERIMENT']['sections']
sectionNames = strSections.split(",")
print(sectionNames)
print("starting " + experiment)

cultivationsSegment = []
allLines = []
prevlines = []
year = ""
inCultivations = False

fileList = os.listdir(srcdocs)
fileList.sort()
lyear = ""
for fname in fileList:
    print("fname: " + fname)
    nyear = fname[0:4]
    
    if int(nyear) >= 1968 and int(nyear) <= 1991 and fname.endswith(".jpg"): 
        allLines = allLines + prevlines
        if nyear != year:
            print("start processing year: " + str(year))
            getOperations(allLines)
            cultivationsSegment = []
            year = nyear
            allLines = []
        
        page = getPageScan(srcdocs + "\\" + fname)
        page = re.sub(" +"," ",page).strip()
        lines = toCorrectedLines(page)
        prevlines = lines
# finalise last
allLines = allLines + prevlines
getOperations(allLines)