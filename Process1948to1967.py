'''
Created on 3 Dec 2018

@author: ostlerr
'''
import os
from YieldBookToData import *
import configparser

#newYear = False

def cleanDate(dirtyDate, year): # date format expects month first for this period
    global lyear
    sDate = ""
    eDate = ""
    if dirtyDate:
        dirtyDate = dirtyDate.replace("=","-").replace("—","-")
        dirtyDate = removePunctuation(str(dirtyDate), ("-"))
        dirtyDate = dirtyDate.replace(" and ",", ")
        print("dirtyDate: " + str(dirtyDate))

        parts = dirtyDate.split(" ")
        if re.match(r"\w{3,5} \d{1,2} - \w{3,5} \d{1,2} \d{4}",str(dirtyDate)):
            lyear = parts[5]
            sDate = "-".join([parts[1],parts[0],lyear])
            eDate = "-".join([parts[4],parts[3],lyear])
        elif re.match(r"\w{3,5} \d{1,2} - \d{1,2} \d{4}",str(dirtyDate)):
            lyear = parts[4]
            month = parts[0]
            sDate = "-".join([parts[1],month,lyear])
            eDate = "-".join([parts[3],month,lyear])
        elif re.match(r"\w{3,5} \d{1,2} - \d{1,2}",str(dirtyDate)):
            month = parts[0]
            sDate = "-".join([parts[1],month,lyear])
            eDate = "-".join([parts[3],month,lyear])
        elif re.match(r"\w{3,5} \d{1,2} \d{1,4}",str(dirtyDate)):
            lyear = parts[2]
            month = parts[0]
            sDate = "-".join([parts[1],month,lyear])        
        elif re.match(r"\w{3,5} \d{1,2}",str(dirtyDate)):
            if lyear == "":
                lyear = str(int(year)-1)
            month = parts[0]
            if (lyear == "" or lyear == str(int(year)-1)) and month in ("Jan","Feb","Mar","April","Apr","May","June","July"):
                lyear = year
            elif lyear == "":
                lyear = str(int(year)-1)

            sDate = "-".join([parts[1],month,lyear])
        else:
            sDate = "UNKNOWN"
            eDate = dirtyDate
            
    return sDate,eDate
  
# this method is all about finding the end of a cultivations segment. If no end is found by the end of the page then carries through to the next page    
def getOperations(lines):
    global cultivationsSegment
    global inCultivations 
    
    for line in lines:
        if(inCultivations):
            if isStop(line): 
                inCultivations = False
                print("ex cultivations")
                break
            else:
                cultivationsSegment.append(line)
        elif fuzz.token_set_ratio(line,"Cultivations, etc.:") >= 75 or year == "1938": 
            cultivationsSegment.clear()
            inCultivations = True 
            print("in cultivations")
            
            parts = line.split(" ")
            if (len(parts) >2):
                line = " ".join(parts[2:])
                cultivationsSegment.append(line)
    processCultivations()
    
def writeJob(sname,opDate,curOp,prevOp):
    if not curOp:   
        curOp = prevOp
    if curOp:
        cleanCurOp = tidyOp(curOp)
        vtype = ""
        if opDate == "variety":
            vtype = "variety"
            cleanCurOp = cleanCurOp.replace("variety:","").strip()
            opDate = ""
        elif cleanCurOp.startswith("note:"):
            vtype = "note"
            cleanCurOp = cleanCurOp.replace("note:","").strip()
        else:
            vtype = "diary record"
        print("opDate: " + str(opDate) + " : " + str(newYear))
        sDate, eDate = cleanDate(opDate,year)
        outfile.write("|".join([str(experiment),str(year),str(sname),str(sDate),str(eDate),vtype,cleanCurOp]))
        outfile.write("\n") 
    return True   
    
    
def tidyOp(line): # Trims leading and trailing punctuation
    nline = line.strip()
    
    if (nline and nline[len(nline)-1] in [",",":","."]):
        nline = nline[0:len(nline)-1]
    
    if (nline and nline[0] in [",",":","."]):
        nline = nline[1:]
    
    nline = nline.strip() 
    return nline

def startsWithBlock(line):
    lline = line.lower()
    if (fuzz.token_set_ratio(lline,"block") >= 75):
        blockParts = line.split(" ",2)
        block = " ".join([blockParts[0],blockParts[1]])
        line = blockParts[2]
        return block, line
    else:
        return None,None        
        
#this method is about subsectioning the cultivations then writing them             
def processCultivations():   #cultivationSections = cultivationxsSegment.split("\n\n")
    # we should already have the cultivations etc removed, but need to test for sections.
    # possible patterns are short lines (<=2 words) and 'section' as second word
    sectionName = ""
    blockName = ""
    subsections = {}
    subsectionText = ""
    for idx, line in enumerate(cultivationsSegment):
       
        #line = line.replace(" and ",", ")
        print(line)
        newBlock, newLine = startsWithBlock(line)
        
        if newBlock:
            blockName = newBlock
            line = newLine.strip()
        newSection = None
        newLine = None
        
        if (line):
            newSection, newLine = startsWithSection(line,sectionNames) 

        if newSection or idx == 0: # Need the zero check in case of no section or dodgy section
            if sectionName: # add the old section name to the dictionary. 
                subsections[sectionName] = subsectionText
            subsectionText = "" #set up the new section text
            sectionName = " ".join([blockName,str(newSection)])
            line = newLine
        
        if (len(line) > 1):
            subsectionText = " ".join([str(subsectionText),line])
            
    if not sectionName:
        sectionName = "All plots"
    subsections[sectionName] = subsectionText           # got a new section...probably
    
    processSections(subsections)
        
def processSections(subsections):
    global lyear
    written = True
    for sname, stext in subsections.items():
        lyear = ""
        print("===========")
        print(sname)
        print(stext)
        print("===========")
        curDate = None
        expectDay = False
        expectDayOrMonth = False
        testYear = False
        prevOp = ""
        curOp = ""
        stext = re.sub(r'(\d{1,2}),',r'\1',stext) # e.g. 1,
        stext = re.sub(r'(\d{4});',r'\1,',stext) # e.g. 1956;
        stext = re.sub(r' [;.:] ',r' ',stext)
        words = stext.split(" ")
        for word in words:
            print(str(word) + " : " + str(testYear) + " : " + str(expectDay) + " : " + str(curDate))
            written = False
            word = word.strip()
            if testYear:
                if word in ("-","—","="):
                    curDate = " ".join([str(curDate),str("-")])
                    testYear = False
                    expectDayOrMonth = True
                elif looksLikeYear(word):
                    curDate = " ".join([str(curDate),str(word)])
                    written = writeJob(sname,curDate,curOp, prevOp)
                    testYear = False
                    expectDay = False
                    print("looks like year: " + curDate)
                    prevOp = curOp if curOp else prevOp
                    curOp = ""
                elif word in months: # same operation, different date
                    written = writeJob(sname,curDate,curOp, prevOp)
                    expectDay = True
                    testYear = False
                    prevOp = curOp if curOp else prevOp
                    curDate = word
                else: # new operation
                    written = writeJob(sname,curDate,curOp, prevOp)
                    curDate = None
                    prevOp = curOp if curOp else prevOp
                    curOp = word 
                    expectDay = False
                    testYear = False
            elif expectDayOrMonth:# this case is for after a dash
                if word in months:
                    expectDay = True
                    curDate = " ".join([str(curDate),str(word)])
                else: 
                    curDate = " ".join([str(curDate),str(word).strip()])
                    testYear = True
                    expectDay = False
                expectDayOrMonth = False
            elif expectDay:
                curDate = " ".join([str(curDate),str(word).strip()])
                testYear = True
                expectDay = False
            elif word in months: # same operation, different date
                expectDay = True
                testYear = False
                curDate = word
            else:
                expectDay = False
                testYear = False
                curOp = " ".join([curOp,word])
            if word.startswith("variety"):
                curDate = "variety"
                curOp = ""
        if curDate == "variety":
            print("variety: " + curOp)
            written = writeJob(sname,curDate,curOp, prevOp)
            curDate = ""
            curOp = ""
    if not written:
        print("not written")
        #newYear = True
        writeJob(sname,curDate,curOp, prevOp)
        curOp = ""

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
strSections = config['EXPERIMENT']['sections']
sectionNames = strSections.split(",")
print(sectionNames)
cultivationsSegment = []
inCultivations = False
sectionStarts = ()
year = ""
newYear = False
lyear = ""

fileList = os.listdir(srcdocs)
fileList.sort()

for idx, fname in enumerate(fileList):
    nyear = fname[0:4]
    if int(nyear) > 1951 and int(nyear) < 1968 and fname.endswith(".jpg"):
         
        print("processing document " + str(idx) + ", " +fname)
        inCultivations = True if (nyear == year) else False
        year = nyear
        page = getPageScan(srcdocs + "\\" + fname)
        page = re.sub(" +"," ",page).strip()
        print(page)
        lines = toCorrectedLines(page)        
        print(lines)
        getOperations(lines)
        
print('done')
outfile.close()