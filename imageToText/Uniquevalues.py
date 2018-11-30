'''
Created on 30 Nov 2018

@author: ostlerr
'''
import numpy as np
import pandas as pd
import re

ybdata = pd.read_csv("D:\\code\\python\\workspace\\YieldBookDataTools\\imageToText\\titleAndObject1994.txt", "|", encoding = "ISO-8859-1")
rawsponsors = ybdata['sponsors'].unique()

p = re.compile("(([A-Z]\.){1,3} [A-Z]{1}[a-z]+)")# need to factor in McG
sponsors = np.delete(rawsponsors, 0)
for sponsor in sponsors:
#    print(sponsor)
    sponsorList = p.findall(sponsor)
    for sp in sponsorList:
        print(sp[0])

