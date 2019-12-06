'''
Created on 30 Nov 2018

@author: ostlerr
'''
import numpy as np
import pandas as pd
import re

line = "Sponsor: R. L. Tata, P. J. K. Fee and D. G. ReMwa blah de blah"

p = re.compile("((?:[A-Z]\. +)+[A-Z]{1}[a-z]+)")# need to factor in McG
sponsorList = p.findall(line)
for sp in sponsorList:
    print(sp)
