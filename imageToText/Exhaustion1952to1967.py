'''
Created on 3 Dec 2018

@author: ostlerr
'''
import os
from imageToText.Process1952to1968 import loopDocs, globals
global sectionStarts
global sectionNames
sectionStarts= ("cropped","fallowed","potatoes","sugar","kale","spring","barley","swedes")
sectionNames = ("cropped section", "fallowed section","potatoes","sugar beet","kale","spring wheat","barley","swedes")
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\ExhaustionLand1952.txt", "w+", 1)
globals(ofOperations,sectionNames, sectionStarts,"Exhaustion Land")
loopDocs("D:\\work\\yieldbooks\\Exhaustion\\")
print('done')
ofOperations.close()