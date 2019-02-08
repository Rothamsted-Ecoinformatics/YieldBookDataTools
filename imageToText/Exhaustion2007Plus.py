'''
Created on 5 Feb 2019

@author: ostlerr
'''
from imageToText.Process2007Plus import loopDocs, globals

print("Exhaustion Land")
global sectionStarts
global sectionNames
#sectionStarts= ("all", "P", "K")
sectionNames = ("all plots", "p test", "k test")
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\ExhaustionLand2007.txt", "w+", 1)
globals(ofOperations, "Exhaustion Land",sectionNames)
loopDocs("D:\\work\\yieldbooks\\Exhaustion\\")
print('done')
ofOperations.close()