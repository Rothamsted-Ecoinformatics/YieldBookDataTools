import cv2
import numpy as np
import pytesseract
from pytesseract.pytesseract import Output
import string
import configparser
import os
import re
import xmltodict

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

#years = {
#    "1993":"53",
#    "1992":"52",
#    "1991":"46",
#    "1990":"52",
#    "1989":"52",
#    "1988":"50",
#    "1987":"57",
#    "1986":"58",
#    "1985":"62",
#    "1984":"68",
#    "1983":"67",
#    "1982":"66",
#    "1981":"65",
#    "1980":"63",
#    "1979":"61",
#    "1978":"80",
#    "1977":"62"
#    }
#years = {
#    "1976":"233757"
#}
#scan
#years = {
#    "1975":"83",
#    "1972":"74",
#    "1970":"83"
#}

#yields 1
#years = {
#    "1974":"83"
#}

#yields 2, numerical
years = {
    "1973":"97",
   "1971":"78",
   "1969":"78"
}

for bk in years:
    start_doc = int(years[bk])
    year = bk
    print(year + ":" + str(start_doc))
    outfile = open("D:\\Work\\rothamsted-ecoinformatics\\yieldbooks\\"+year+".xml", "w+", 1)

    dir = "X:\\YieldBook"+year+"\\pages"
    fileList = os.listdir(dir)
    fileList.sort()

    outfile.write("<experiments>")

    outfile.write("\n<experiment>\n<![CDATA[")
    exp = ""
    for fname in fileList:
        print("fname: " + fname)
        i = 0
        
        fp = fname.split("_") # yields 1
        #i = int(fname.split("_")[1]) # yields 2
        #if re.match("scan[0-9][0-9][0-9]",fname):
         #   i = int(fname[4:7])
        #if re.match("PC[0-9][0-9][0-9]",fname):
        #    i = int(fname[2:8])
        if len(fp) == 2:
            i = int(fp[1].split(".")[0])
        
        if  i >= start_doc: 
            content = getPageScan(dir + "\\" + fname)
            if content.find("Object:") >-1: 
                outfile.write("\n]]></experiment>")
                outfile.write("\n<experiment>\n<![CDATA[")
                outfile.write("\n")
                outfile.writelines(exp)
                exp = content
            else:
                exp = "\n".join([exp,content])
    outfile.write("\n]]></experiment>\n</experiments>")
    outfile.close()

print("done")