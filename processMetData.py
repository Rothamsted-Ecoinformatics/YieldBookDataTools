'''
Created on 1 Jul 2019

@author: ostlerr
'''
import os
from YieldBookToData import getPageScan, correctWords, removePunctuation
import configparser
import re
from fuzzywuzzy import fuzz

config = configparser.ConfigParser()
print(config.read('D:\Code\python\workspace\YieldBookDataTools\imageToText\config.ini'))
#experiment = config['EXPERIMENT']['name']
#outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']

fileList = os.listdir(srcdocs)
fileList.sort()
treatments = []
for fname in fileList:
    nyear = fname[12:16]
    #npage = fname[4:6]
    #print (nyear + " - " + npage)
    print(srcdocs + "\\" + fname)
    
    if fname=="1975.jpg":
        outfile = open(srcdocs + "/"+nyear+".txt", "w+", 1)
        page = getPageScan(srcdocs + "\\" + fname)
        lines = page.split("\n")
        for line in lines:
            data = line.split(" ")
            outfile.write(nyear)
            for d in data:
                d = d.replace("{","(").replace("}",")").replace("(,","(")
                outfile.write("," + d)
            outfile.write("\n")
        print(page)