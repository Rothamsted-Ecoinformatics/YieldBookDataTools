'''
Created on 8 Feb 2019

@author: ostlerr
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
import string
import configparser

def loopDocs():
    year = ""
    fileList = os.listdir(srcdocs)
    fileList.sort()
    corrections = []
    
    with open("D:\\Work\\rothamsted-ecoinformatics\\YieldbookDatasetDrafts\\seedCorrections.csv", 'r') as infile:
        for line in infile:
            corrections.append(line.strip())
    
    for fname in fileList:
        nyear = fname[0:4]
        
        print("year = " + nyear)
        if int(nyear) >= 1972 and int(nyear) <= 1991 and fname.endswith(".jpg"): 
            page = getPageScan(srcdocs + "\\" + fname)
            page = correctWords(page.replace("\n"," ").split(" "),corrections)
            #page = correctWords(page.replace("\n","$$").split(" "),corrections)
            data = False
            
            print("year: " + page)
            if page.find("Seed:") > -1:# or page.find("$$Seed") > -1:
                data = True
                #page = page.replace("$$", " ")
                page = page[page.find("Seed:")+5:] # this should stop everything before the Cultivations from being processed
                if page.find("Cultivations") > -1:
                    page = page[:page.find("Cultivations")]
                page = page.strip() 
                
            print(data)
            if data:
                words = page.split(" ")
                cropSection = None
                curinfo = ""
                for idx, word in enumerate(words):
                    testWord = removePunctuation(word.lower(),[])
                    if testWord in ["potatoes","wheat","beans","wheats","barley"]:
                        print ("found: " + testWord)
                        #test the previous word - This will be handy for standard applications
                        if idx > 0:
                            testPrevWord = removePunctuation(words[idx-1].lower(),[])
                            if testPrevWord in ["spring","winter","w"]:
                                testWord = " ".join([testPrevWord,testWord])
                                curinfo = curinfo[:curinfo.find(testPrevWord)]
                        if curinfo and cropSection:
                            outfile.write(experiment + "|" + str(nyear) + "|" + cropSection + "|" + curinfo) 
                            outfile.write("\n")
                        cropSection = testWord
                        curinfo = ""
                    else:
                        curinfo = " ".join([curinfo,word])
                    print(str(cropSection) + ": " + str(curinfo))
                outfile.write(experiment + "|" + str(nyear) + "|" + str(cropSection) + "|" + curinfo) 
                outfile.write("\n")        
                
config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']
loopDocs()