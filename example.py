import pytesseract
import cv2
import numpy as np
from pytesseract.pytesseract import Output

img = cv2.imread('D:\\Code\\python\\workspace\\YieldBookDataTools\\Text Mining\\YieldBook1965_010.jpg')


img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

kernel = np.ones((2, 2), np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.bilateralFilter(img,9,70,70)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
img = cv2.GaussianBlur(img, (1, 1), 0)
img = cv2.fastNlMeansDenoising(img,None,9,21,5)

#
#img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#img = cv2.cvtColor(img, cv2.THRESH_BINARY)
cv2.imwrite('img.jpg',img)
scan = pytesseract.image_to_string(img, lang='lat+eng', config='--dpi 300 --psm 4',nice=0,output_type=Output.DICT)

# need to get the current experiment from code and check it
# get year
words = scan.get("text").replace("\n"," ").split(" ")
lines = " ".join(words).split(".")
for item in lines:
    #look for a pattern of upper case which indicates a change in the cultivated thing 
    print(item)