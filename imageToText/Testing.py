'''
Created on 3 Dec 2018

@author: ostlerr
'''
from imageToText.YieldBookToData import enhance, getSponsors
import pytesseract
import re
from pytesseract.pytesseract import Output

job = "12-Aug-07 a_ blajsj shsh"

code = re.search(r".?[apfs].? ", job) # need to expand this to search just part of the string and clean up the value

print(code)
r= re.compile(r"[^apfs]")

val = r.sub("",code.group(0)) # this works
print(val)