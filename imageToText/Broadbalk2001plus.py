'''
Created on 29 Nov 2018

Covers 2007 onwards. Has greater separation of applications for treatment, rate and unit

These documents only cover the Classicals and other long-terms, main concern is to extract the experimental diary

@author: ostlerr
'''
from imageToText.Process2001Plus import loopDocs, globals

print("starting Broadbalk 2001")
#global sectionStarts
#global sectionNames
#sectionStarts= ("ley","lucerne","rye","hay","barley","sugar","potatoes","spring","sainfoin","seeds","carrots","turnips","seed","clover","winter","grass","fallow","oats","s","w")
sectionNames = ("winter wheat","woats","fallow section 8","winter oats","maize","fallows","sections","s wheat","s oats","all sections", "w wheat", "w oats", "forage maize", "wilderness")
outfile = open("D:\\Work\\rothamsted-ecoinformatics\\Lists\\Broadbalk2003-6.txt", "w+", 1)
globals(outfile,"Broadbalk",sectionNames)
loopDocs("D:\\work\\yieldbooks\\broadbalk\\")
print('done')
outfile.close()