'''
Created on 3 Dec 2018

@author: ostlerr
'''
import re
from enum import Enum

class Was(Enum):
    none = 0
    initital = 1
    title = 2
    name = 3
    
s = "J. A. CURRIE, Ph.D.(Dunelm)"
namebits = s.split(",",1)
print(namebits)
names = []
name = ""

last = Was.none
for idx, bit in enumerate(namebits):
    #print(idx)
    #print(re.match(r"[A-Z]\.",bit))
    print(bit)
    current = 0
    if re.match(r"[A-Z]\.",bit):
        current = Was.initital
    elif re.match(r"[\w]{2,3}(\.|,)", bit):
        current = Was.title
    elif re.match(r"[A-Z]{3,}", bit):
        current = Was.name
    elif re.match(r"[a-zA-Z]{3,}", bit):
        current = Was.name
        
    if idx == 0:
        print("a")
        name = bit
    elif last == Was.initital and current == Was.initital:
        print("b")
        name = " ".join([name, bit])
    elif last == Was.initital and current == Was.name:
        print("c")
        name = " ".join([name, bit])
        names.append(name)
        name = ""
    elif current == Was.title:
        if len(name) > 0:
            print("d")
            names.append(name)
        else:
            print("e")
            name = bit
    elif last == Was.name and current == Was.initital:
        print("f")
        if len(name)>0:
            names.append(name)
        name = bit        
    else:
        print("g")
        name = " ".join([name, bit])
    last = current
names.append(name)

for n in names:
    print(n)