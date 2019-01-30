'''
Created on 3 Dec 2018

@author: ostlerr
'''
import os
from imageToText.Process1952to1968 import loopDocs, globals
global sectionStarts
global sectionNames
sectionStarts= ("ley","lucerne","rye","hay","barley","sugar","potatoes","spring","sainfoin","seeds","carrots","turnips", "seed")
sectionNames = ("spring wheat (replacing rye)", "spring wheat","sainfoin 3rd year","sainfoin 2nd year","sainfoin 1st year","seeds hay","carrots","turnips (after carrots failed) 3rd course","carrots 3rd course","seed hay 3rd course","barley 2nd test crop","potaoes 1st test crop","sugar beet 3rd course","hay 3rd course","rye 2nd course","potatoes 1st course","lucerne 3rd year","lucerne 2nd year","lucerne 1st year","ley 3rd year","ley 2nd year","ley 1st year","ley - first year", "ley - second year","lucerne - first year","lucerne - second year", "potatoes","rye","barley","ley - third year", "hay", "sugar beet")
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\WLA1952.txt", "w+", 1)
globals(ofOperations,sectionNames, sectionStarts,"Woburn Ley Arable")
loopDocs("D:\\work\\yieldbooks\\WLA\\")
print('done')
ofOperations.close()