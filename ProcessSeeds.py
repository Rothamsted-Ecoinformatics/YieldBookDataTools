'''
Created on 8 Feb 2019

@author: ostlerr
'''
import os
from YieldBookToData import correctWords, removePunctuation
import configparser
import re
import xmltodict

def applyCorrections(content):
    # Note this preserves lines as they provide structural cues to help with processing
    # some special force replacements - these could be applied to the whole doc
    content = re.sub(" +"," ",content).strip()
    content = re.sub(r"(\d),(\d)",r"\1.\2",content) # decimals
    return correctWords(content)

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['seeds_outfile'], "w+", 1)
srcdoc = config['EXPERIMENT']['raw_xml']
crops = config['EXPERIMENT']['crops'].split(",")

with open(srcdoc) as fd:
    doc = xmltodict.parse(fd.read())

for rep in doc["reports"]["report"]:
    year = rep["year"]

    if int(year) >= 1972 and int(year) <= 1991: 
        content = rep["rawcontent"]
        data = False
        if content.find("Seed:") > -1:# or page.find("$$Seed") > -1:
            data = True
            content = content[content.find("Seed:")+5:] # this should stop everything before the Cultivations from being processed
            content = applyCorrections(content) # applying corrections before finding seed can cause problems. 
            if content.find("Cultivations") > -1:
                content = content[:content.find("Cultivations")]
            content = content.strip() 
            
            content = content.replace("\n"," ")
        if data:
            words = content.split(" ")
            words = list(filter(None,words))
            cropSection = None
            curinfo = ""
            #print(words)
            #print(crops)
            for idx, word in enumerate(words):
                #print(word + " : " + curinfo)
                testWord = removePunctuation(word.lower(),[])
                if crops[0] != "" and testWord in crops:
                    print("<<<<<<<<<<<<<is crop")
                    #test the previous word - This will be handy for standard applications
                    if idx > 0:
                        testPrevWord = removePunctuation(words[idx-1].lower(),[])
                        if testPrevWord in ["spring","winter","w","forage"]:
                            testWord = " ".join([testPrevWord,testWord])
                            curinfo = curinfo[:curinfo.find(testPrevWord)]
                    if curinfo and cropSection:
                        outfile.write(experiment + "|" + str(year) + "|" + cropSection + "|" + curinfo.strip()) 
                        outfile.write("\n")
                    cropSection = testWord
                    curinfo = ""
                    print(">>>>>>>>>>>>" + testWord)
                else:
                    curinfo = " ".join([curinfo,word])
            print("**************")
            print (curinfo)        
            outfile.write(experiment + "|" + str(year) + "|" + str(cropSection) + "|" + curinfo.strip()) 
            outfile.write("\n")        