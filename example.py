import pytesseract
import cv2
from pytesseract.pytesseract import Output

img = cv2.imread('D:\\work\\tesseract\\testing\\scan009.jpg')
img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.fastNlMeansDenoising(img,None,7,21,10)
img = cv2.bilateralFilter(img,9,70,70)

#img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imwrite('img.jpg',img)
scan = pytesseract.image_to_string(img, lang='lat+eng', config='--dpi 200 --psm 4',nice=0,output_type=Output.DICT)

lines = scan.get("text").split("\n")
print(lines)
