'''
Created on 3 Dec 2018

@author: ostlerr
'''
from imageToText.YieldBookToData import enhance, getSponsors
import pytesseract
import re
from pytesseract.pytesseract import Output

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

line = "Oultivations, ctc,:"
parts = line.split(" ")

print(len(parts))
print(parts)

tString = "Oultivations, ctc,:"
#tString = " "
#print(fuzz.toke_sort_ratio("fortilizors","fertilizers"))

parts = re.split(r"[:.,]",tString,1)
print("1 split: " + str(parts))
sectionKeywords = ("soction", "Barley", "Sugar beet", "Clover", "Wheat", "Potatoes", "Rye")
paragraphStartKeyWords = ("Cultivations, etc.:", "section", "jim","bob")
months = ("cwt","Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
print("zug---------------")
matched = process.extractBests("owt",months,scorer=fuzz.partial_ratio, score_cutoff=5) 
print(matched)
matched = process.extractBests("owt",months,scorer=fuzz.ratio, score_cutoff=5) 
print(matched)
matched = process.extractBests("owt",months,scorer=fuzz.token_set_ratio, score_cutoff=5)
print(matched)
matched = process.extractBests("owt",months,scorer=fuzz.token_sort_ratio, score_cutoff=5)
print(matched)
matched = process.extractBests("owt",months,scorer=fuzz.QRatio, score_cutoff=5)
print(matched)
print("---------------")

print("---------------")
matched = fuzz.partial_ratio(tString,"Cultivations, etc.:") 
print(matched)
matched = fuzz.ratio(tString,"Cultivations, etc.:") 
print(matched)
matched = fuzz.token_set_ratio(tString,"Cultivations, etc.:")
print(matched)
matched = fuzz.token_sort_ratio(tString,"Cultivations, etc.:")
print(matched)
matched = fuzz.WRatio(tString,"Cultivations, etc.:")
print(matched)
print("---------------")

if matched:
    print(tString + ": " + str(matched))
else: 
    print("arse")
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