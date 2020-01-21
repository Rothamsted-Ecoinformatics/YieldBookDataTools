'''
Created on 18 Jun 2019

@author: ostlerr
'''
import re


test = "Barclay Gallup 360 4.00 V200 I/ha "
parts = test.split(" ")
l = len(parts)
print(parts[l-1])
print(parts[l-2])
print(parts[l-3])
print(re.match(r"[\d]+\.?[\d]?",parts[l-3]))
print (str.isnumeric("1.0"))


t = []
print(t.pop())









if(re.search(r"[:.>;]\s?[~—@PTBOo\d]{1,2}\s?[:.>;]"," : T : P : P test (triple superphosphate at 98 kg, plots").start()>-1):
    print("true")


p = re.compile(".*(BEN A).*")

s = "FUNGCIDE, NONE SF S BEN A BEN S BENtSF S NUA A NUA S MEAN"
#for word in s.split(" "):
print(p.match(s))

line = re.sub(r' [;] ',r' ',"Sept 28 - Oct 8, 1956, Apr 3 - 5, ; 1957, June 25")
print(line)

dd = "May 12 - 15 156"

x = re.match("\w{3,5} \d{1,2} - \d{1,2} \d{4}",dd)
print(x)
