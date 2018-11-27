from PIL import Image, ImageFilter, ImageEnhance
    
import pytesseract

im = Image.open('D:\\work\\tesseract\\testing\\scan009.jpg')


#im = im.filter(ImageFilter.EDGE_ENHANCE)
#im = im.filter(ImageFilter.BLUR)

im=im.filter(ImageFilter.MedianFilter(1))

thresh = 200
fn = lambda x : 255 if x > thresh else 0
im = im.convert('L').point(fn, mode='1')

im=im.filter(ImageFilter.MedianFilter(1))

im.save("mf4.jpg")
print(pytesseract.image_to_string(im, lang='lat+eng', config='--dpi 300 --psm 4'))









