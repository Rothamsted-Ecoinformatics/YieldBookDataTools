'''
Created on 3 Dec 2018

@author: ostlerr
'''
from imageToText.Process1968to1991 import loopDocs, globals

print("starting WLA")
global sectionStarts
global sectionNames
sectionStarts= ("ley","lucerne","rye","hay","barley","sugar","potatoes","spring","sainfoin","seeds","carrots","turnips","seed","clover","winter","grass","fallow","oats","s","w")
sectionNames = ("sainfoin 3rd year","sainfoin 2nd year","sainfoin 1st year","seeds hay","carrots",
                "turnips (after carrots failed) 3rd course","carrots 3rd course","seed hay 3rd course",
                "sugar beet 3rd course","hay 3rd course","rye 2nd course","lucerne 3rd year","lucerne 2nd year","lucerne 1st year",
                "ley 3rd year","ley 2nd year","ley 1st year","ley - first year", "ley - second year","ley - third year","ley 2nd and 3rd years",
                "lucerne - first year","lucerne - second year", 
                "rye", "hay", "sugar beet",
                "s barley 1st and 2nd treatment crops","s barley 2nd test crop","barley","barley 2nd test crop","barley 3rd treatment crop","barley 2nd treatment crop","barley 1st and 2nd treatment crops",
                "potatoes 1st test crop","potatoes","potatoes 1st course","potatoes 1st treatment crop",
                "w wheat 1st test crop","spring wheat (replacing rye)","spring wheat","wheat 2nd test crop","winter wheat","winter wheat 1st test crop",
                "clover 1st year, clover 2nd and 3rd years", "clover 2nd year", "clover 3rd year",
                "grass ley and clover/grass ley 1st year","grass ley and clover/grass ley 2nd year","grass ley and clover/grass ley 3rd year","grass ley and clover grass/ley 2nd 3rd 4th 5th and 6th years","grass ley and clover grass/ley 2nd 3rd 4th 5th 6th 7th and 8th years"
                "s oats","oats 3rd treatment crop",
                "s beans 3rd treatment crop","s beans/potatoes 3rd treatment crop",
                "w beans 3rd treatment crop",
                "fallow 1st and 2nd treatment years","fallow 1st treatment year","fallow 2nd treatment year")
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\WLA1968.txt", "w+", 1)
globals(ofOperations,sectionNames, sectionStarts,"Woburn Ley Arable")
loopDocs("D:\\work\\yieldbooks\\WLA\\")
print('done')
ofOperations.close()