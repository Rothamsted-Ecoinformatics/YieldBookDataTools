'''
Created on 26 Apr 2019

@author: ostlerr
'''
import os
from imageToText.YieldBookToData import getPageScan, correctWords, removePunctuation
import configparser
import re

config = configparser.ConfigParser()
config.read('config.ini')
experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']

fileList = os.listdir(srcdocs)
fileList.sort()

for fname in fileList:
    nyear = fname[0:4]

    if int(nyear) >= 1968 and int(nyear) <= 1991 and fname.endswith(".jpg"): 
        page = getPageScan(srcdocs + "\\" + fname)
        page = correctWords(page.replace("\n"," ").split(" "))
        data = False

        if page.find("NOTES:") > -1:# or page.find("$$Seed") > -1:
            data = True
            page = page[page.find("NOTES:")+6:] # this should stop everything before the Cultivations from being processed
            if page.find("Basal") > -1:
                page = page[:page.find("Basal")]
            elif page.find("GRAIN") > -1:
                page = page[:page.find("GRAIN")]
            page = page.strip() 
            
        print(page)
        notes = []
        if data:
            words = page.split(" ")
            curNote = ""
            noteId = ""
            for idx, word in enumerate(words):
                if re.match(r"\([1-9]\)",word):
                    noteId = word
                    if (noteId != ""):
                        notes.append(curNote)
                        curNote = ""
                else:
                    curNote = " ".join([curNote,word])
            notes.append(curNote)
            for note in notes:        
                outfile.write(experiment + "|" + str(nyear) + "|" + note) 
                outfile.write("\n")        