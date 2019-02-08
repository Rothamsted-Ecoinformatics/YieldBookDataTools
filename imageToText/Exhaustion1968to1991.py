'''
Created on 3 Dec 2018

@author: ostlerr
'''
from imageToText.Process1968to1991 import loopDocs, globals

print("starting Exhaustion Land")
global sectionStarts
global sectionNames
global sectionStops
sectionStarts= ("")
sectionNames = ("")
sectionStops = ("PHOSPHATE PLOTS","GRAIN TONNES/HECTARE","SUMMARY OF RESULTS","TABLE OF MEANS")
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\Exhaustion1968.txt", "w+", 1)
globals(ofOperations,sectionNames, sectionStarts,sectionStops,"Exhaustion Land")
loopDocs("D:\\work\\yieldbooks\\Exhaustion\\")
print('done')
ofOperations.close()