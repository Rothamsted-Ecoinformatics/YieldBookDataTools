import cv2
import numpy as np
import pytesseract
from pytesseract.pytesseract import Output
import string
import configparser
import os

    
    #img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #img = cv2.medianBlur(img,3)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    #img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    #return img

#def getPageScan(pathToFile):
#    img = enhance(pathToFile) # use --psm 6 for normal use lat/eng
#    scan = pytesseract.image_to_string(img, lang='eng', config='--dpi 600 --psm 6',nice=0,output_type=Output.DICT)
#    page = scan.get("text")
#    return page
fname = "D:\\Work\\rothamsted-ecoinformatics\\WRN20\\Scanplots.png"

img = cv2.imread(fname)
#img = cv2.blur(img,(3,3)) # OK
#img = cv2.medianBlur(img,3)
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
kernel = np.ones((3,3),np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#cv2.imshow("pic",img)

#
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#kernel = np.ones((1, 1), np.uint8)
#img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#print(img)
#scan = pytesseract.image_to_string(img, lang='eng', config='--dpi 600 --psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
#scan = pytesseract.image_to_string(img,config='-c preserve_interword_spaces=1x1 --dpi 1200 --psm 6 --oem 3')
scan = pytesseract.image_to_string(img, lang='eng', config='--dpi 300 --psm 6',nice=0,output_type=Output.DICT)
   
#page = scan.get("text")
print(scan)

#hocr = pytesseract.image_to_pdf_or_hocr(fname, extension='hocr')

outfile = open("D:\\Work\\rothamsted-ecoinformatics\\WRN20\\Scanplots.txt", "w+", 1)
outfile.writelines(scan.get("text"))
