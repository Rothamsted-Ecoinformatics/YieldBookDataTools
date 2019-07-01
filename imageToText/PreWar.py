'''
Created on 30 Apr 2019

@author: ostlerr
'''
import os
from imageToText.YieldBookToData import getPageScan, correctWords, removePunctuation
import configparser
import re

config = configparser.ConfigParser()
config.read('config.ini')
#experiment = config['EXPERIMENT']['name']
#outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']

fileList = os.listdir(srcdocs)
fileList.sort()

for fname in fileList:
    nyear = fname[0:4]
    npage = fname[4:6]
    print (nyear + " - " + npage)
    page = getPageScan(srcdocs + "\\" + fname)
    print(page)