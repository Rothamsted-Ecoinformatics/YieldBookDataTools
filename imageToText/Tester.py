'''
Created on 18 Jun 2019

@author: ostlerr
'''
import re

p = re.compile(".*(BEN A).*")

s = "FUNGCIDE, NONE SF S BEN A BEN S BENtSF S NUA A NUA S MEAN"
#for word in s.split(" "):
print(p.match(s))