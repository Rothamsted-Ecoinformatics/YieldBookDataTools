'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to extract the experimental diary

@author: ostlerr
'''
from imageToText.Process1992to2006 import loopDocs, globals

print("Exhaustion Land")
global sectionStarts
global sectionNames
#sectionStarts= ("all", "P", "K")
sectionNames = ("all plots", "p test", "k test")
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\ExhaustionLand1992.txt", "w+", 1)
globals(ofOperations,sectionNames, "Exhaustion Land")
loopDocs("D:\\work\\yieldbooks\\Exhaustion\\")
print('done')
ofOperations.close()