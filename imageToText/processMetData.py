'''
Created on 1 Jul 2019

@author: ostlerr
'''
import os
from imageToText.YieldBookToData import getPageScan, correctWords, removePunctuation
import configparser
import re
from fuzzywuzzy import fuzz

config = configparser.ConfigParser()
config.read('config.ini')
#experiment = config['EXPERIMENT']['name']
outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']

fileList = os.listdir(srcdocs)
fileList.sort()
treatments = []
for fname in fileList:
    #nyear = fname[0:4]
    #npage = fname[4:6]
    #print (nyear + " - " + npage)
    print(srcdocs + "\\" + fname)
    
    if fname.endswith("jpg"):
        page = getPageScan(srcdocs + "\\" + fname)
        lines = page.split("\n")
        for line in lines:
            data = line.split(" ")
            for d in data:
                outfile.write(d + ",")
            outfile.write("\n")
        print(page)