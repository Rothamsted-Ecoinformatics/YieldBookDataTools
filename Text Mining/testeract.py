from PIL import Image, ImageFilter, ImageEnhance
    
import pytesseract
import cv2

im = cv2.imread('D:\\work\\tesseract\\testing\\scan009.jpg')

gray = im
gray = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
gray = cv2.bilateralFilter(gray,9,70,70)
gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
gray2 = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
#gray = cv2.medianBlur(gray,1)
#gray = cv2.fastNlMeansDenoising(gray,None,7,21,5)


#gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#gray2 = cv2.medianBlur(gray, 3) 

#im = im.filter(ImageFilter.EDGE_ENHANCE)
#im = im.filter(ImageFilter.BLUR)

#im=im.filter(ImageFilter.MedianFilter(1))

#thresh = 200
#fn = lambda x : 255 if x > thresh else 0
#im = im.convert('L').point(fn, mode='1')

#im=im.filter(ImageFilter.MedianFilter(1))

#im.save("mf4.jpg")
#print(pytesseract.image_to_string(im, lang='lat+eng', config='--dpi 300 --psm 4'))
cv2.imshow("graypic", gray2)
#cv2.imshow("gray2", gray2)
cv2.waitKey(0)
print(pytesseract.image_to_string(gray, lang='lat+eng', config='--dpi 300 --psm 4'))

#print(pytesseract.image_to_string(gray2, lang='lat+eng', config='--dpi 300 --psm 4'))







