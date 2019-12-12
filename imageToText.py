import cv2
import numpy as np
import pytesseract
from pytesseract.pytesseract import Output
import string
import configparser
import os

def enhance(fname):
    img = cv2.imread(fname)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img = cv2.medianBlur(img,3)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    return img

def getPageScan(pathToFile):
    img = enhance(pathToFile) # use --psm 6 for normal use lat/eng
    scan = pytesseract.image_to_string(img, lang='eng', config='--dpi 300 --psm 6',nice=0,output_type=Output.DICT)
    page = scan.get("text")
    return page

config = configparser.ConfigParser()
config.read('config.ini')
outfile = open(config['EXPERIMENT']['raw_xml'], "w+", 1)
srcdocs = config['EXPERIMENT']['srcdocs']

fileList = os.listdir(srcdocs)
fileList.sort()
year = ""
outfile.write("<reports>")
rawcontent = ""
for fname in fileList:
    print("fname: " + fname)
    nyear = fname[0:4]
    
    if int(nyear) >= 1948 and int(nyear) <= 2018 and fname.endswith(".jpg"): 
        curcontent = getPageScan(srcdocs + "\\" + fname)
        print(nyear)
        if nyear != year:
            print (year + " " + nyear)
            if rawcontent:
                outfile.write("\n<report>")
                outfile.write("\n<year>" + year + "</year>")
                outfile.write("\n<rawcontent>\n<![CDATA[")
                outfile.writelines(rawcontent)
                outfile.write("\n]]></rawcontent>")
                outfile.write("\n</report>")            
            year = nyear
            rawcontent = curcontent
        else:
            rawcontent += "\n" + curcontent
        
outfile.write("\n<report>")
outfile.write("\n<year>" + year + "</year>")
outfile.write("\n<rawcontent>\n<![CDATA[")
outfile.writelines(rawcontent)
outfile.write("\n]]></rawcontent>")
outfile.write("\n</report>")
outfile.write("\n</reports>")
outfile.close()
print("done")