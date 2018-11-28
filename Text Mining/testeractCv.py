from PIL import Image, ImageFilter
from pylab import *
import rof
import cv2
import pytesseract

ims = Image.open('D:\\work\\tesseract\\testing\\scan009.jpg').convert('L')
ims = ims.filter(ImageFilter.SHARPEN)
thresh = 250
fn = lambda x : 255 if x > thresh else 0
ims.point(fn, mode='1')
im = array(ims)

#im = im.convert('L').point(fn, mode='1')


U,T1 = rof.denoise(im,im,0.2,0.125,100)
figure()
gray()
imshow(U)
axis('equal')
axis('off')
show()

show()
#pil_im = Image.fromarray(U)
#pil_im.save("rof"+str(i*10)+".jpg")
nim = Image.fromarray(U)
print(pytesseract.image_to_string(nim, lang='lat+eng', config='--dpi 200 --psm 4'))
