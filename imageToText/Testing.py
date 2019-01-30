'''
Created on 3 Dec 2018

@author: ostlerr
'''
from imageToText.YieldBookToData import enhance, getSponsors
import pytesseract
import re
from pytesseract.pytesseract import Output
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

months = ("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")

def formatDate(day,month,year):
    d = ""
    if month in ["Sept","Oct","Nov","Dec"]:
        d = "-".join([day,month,str(int(year)-1)])
    else:
        d = "-".join([day,month,year])
    return d, month

def cleanDate(dirtyDate, year):
    sDate = ""
    eDate = ""
    
    dates = dirtyDate.split("-")
    if len(dates) == 1: # just one date
        parts = dates.strip().split(" ")
        if len(parts) == 2 or len(parts) == 3:
            sDate = formatDate(parts[1],parts[0],year)
        else:
            sDate = dirtyDate    
    elif len(dates) == 2:
        sparts = dates[0].strip().split(" ")
        mnth = ""
        if len(sparts) == 2 or len(sparts) == 3:
            sDate, mnth = formatDate(sparts[1],sparts[0],year)
        else:
            sDate = dirtyDate
        
        eparts = dates[1].strip().split(" ")
        if len(eparts) == 1:
            eDate,month = formatDate(eparts[0],mnth,year)
        else:
            if eparts[0] in months:
                eDate,month = formatDate(eparts[1],eparts[0],year)
            else:
                eDate,month = formatDate(eparts[0],mnth,year)
    return dirtyDate,sDate,eDate    


curOpDate = "12-APR-00"
tdate = ""
if curOpDate.endswith("00"):
    tdate = curOpDate.replace("00","2000")
else: 
    tdate = curOpDate[:7] + "19" + curOpDate[7:]
print(tdate)

print(cleanDate("Nov 18-27 1952", "1960"))
print(cleanDate("Nov 18 - 27 1952", "1960"))
print(cleanDate("Nov 18 - Dec 27 1952", "1960"))
print(cleanDate("Nov 18 - Dec 27 1952", "1960"))
print(cleanDate("May 18-27", "1960"))
print(cleanDate("May 18 - 27", "1960"))

word = "198h"
for c in word:
    print(c)
print(word[0:2])



line = "bals  ajkas ajkskjs akjsakj EX A2"
parts = re.split(r"[()/]",line)
print(parts)
cmc = re.compile(r"(.{2}/.{1})")
cmcl = cmc.findall("blah c bla Cb/1")

fname = "YieldBook1952_004"
print(fname[9:13])

print(cmcl)

corrections = []
with open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\corrections.csv", 'r') as infile:
    for line in infile:
        corrections.append(line.strip())
print(corrections)
    #for row in reader:
       # corrections.append(row)

for avg in range(0,10):
    print(avg)
    
print("xxxxxxxxxxxxxx")

print(re.search(r"[0-9]","1"))

line = "Oultivations, ctc,:"
parts = line.split(" ")

print(len(parts))
print(parts)

tString = "Oultivations, ctc,:"
#tString = " "
#print(fuzz.toke_sort_ratio("fortilizors","fertilizers"))

parts = re.split(r"[:.,]",tString,1)
print("1 split: " + str(parts))
sectionKeywords = ("ley","rye","hay")#("ley - first year", "ley - second year","lucerne - first year","lucerne - second year", "potatoes","rye","barley","ley - third year", "hay", "sugar beet")
paragraphStartKeyWords = ("Cultivations, etc.:", "section", "jim","bob")
line = "ley" #"ley - third year grazed by sheep 6 circuits  May 19"
months = ("cwt","Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
print("zug---------------")
matched = process.extractOne(line,sectionKeywords,scorer=fuzz.token_set_ratio,score_cutoff=50)
print(matched)
matched = process.extractOne(line,sectionKeywords,scorer=fuzz.partial_ratio, score_cutoff=5) 
print(matched)
matched = process.extractOne(line,sectionKeywords,scorer=fuzz.ratio, score_cutoff=5) 
print(matched)
matched = process.extractOne(line,sectionKeywords,scorer=fuzz.token_set_ratio, score_cutoff=5)
print(matched)
matched = process.extractBests(line,sectionKeywords,scorer=fuzz.token_sort_ratio, score_cutoff=5)
print(matched)
matched = process.extractBests(line,sectionKeywords,scorer=fuzz.QRatio, score_cutoff=5)
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