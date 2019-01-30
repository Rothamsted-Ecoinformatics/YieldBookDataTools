'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to extract the experimental diary

@author: ostlerr
'''
from imageToText.Process1968to1991 import loopDocs, globals

print("starting WLA")
global sectionStarts
global sectionNames
sectionStarts= ("ley","lucerne","rye","hay","barley","sugar","potatoes","spring","sainfoin","seeds","carrots","turnips","seed","clover","winter","grass","fallow","oats","s","w")
sectionNames = ("grass ley and clover/grass ley 4th year (rotation LLN4 and LLC4",
                "grass ley and clover/grass ley 1st year (rotation LN1 LC1 LLN1 and LLC1)",
                "grass leys 2nd 3rd 5th 6th 7th and 8th years (rotation LN2-3 LLN2-3 and LLN5-8)",
                "clover grass leys 2nd 3rd 5th 6th 7th and 8th years (rotation LC2-3 LLC2-3 and LLC5-8)",
                "s barley 1st and 2nd treatment crops (rotation AB)",
                "w beans 3rd treatment crop (rotation AF and AB)"
                
                
                
                ,"grass ley and clover/grass ley 2nd year","grass ley and clover/grass ley 3rd year","grass ley and clover grass/ley 2nd 3rd 4th 5th and 6th years","grass ley and clover grass/ley 2nd 3rd 4th 5th 6th 7th and 8th years"
                "s oats","oats 3rd treatment crop",
                "s beans 3rd treatment crop","s beans/potatoes 3rd treatment crop",
                "w beans 3rd treatment crop",
                "fallow 1st and 2nd treatment years","fallow 1st treatment year","fallow 2nd treatment year")
ofOperations = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\WLA1992.txt", "w+", 1)
globals(ofOperations,sectionNames, sectionStarts,"Woburn Ley Arable")
loopDocs("D:\\work\\yieldbooks\\WLA\\")
print('done')
ofOperations.close()