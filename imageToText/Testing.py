'''
Created on 3 Dec 2018

@author: ostlerr
'''
from imageToText.YieldBookToData import enhance, getSponsors
import pytesseract
import re
from pytesseract.pytesseract import Output

job = "12 Aug 07 a_ blajsj   shsh sdjdk\n skdskdsl  skdsd l" 

job = job + " " + "blaj"

jobparts = job.split()
months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
for part in jobparts:
    if part in months:
        print("Yes")
    else: 
        print ("No")

newJob = " ".join(job.split())
print(newJob)

code = re.search(r".?[apfs].? ", job) # need to expand this to search just part of the string and clean up the value

print(code)
r= re.compile(r"[^apfs]")

val = r.sub("",code.group(0)) # this works
print(val)