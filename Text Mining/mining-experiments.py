import PyPDF2
import re

pdfFileObj = open('YieldBook2016_Part7.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
p_text = pageObj.extractText()
functionlist = ['f','h','adj','i','gr','foliar ','m','water conditioner']
unitslist = ['g/l','w/w','w/v']

#number of elements should be 37...

#returns list but only for this page of 2016 because the
#extra entries have length<3
def findtradenames(string):
    w = string.splitlines()
    z=[]
    for line in w:
        if (line[0].isupper() == True):
            z.append(line)
        for zline in z:
            if (len(zline) <= 2) == True:
                z.remove(zline)
    return z

#returns full list when functionlist correct
def findfunctions(string):
    a = string.splitlines()
    b = []
    for line in a:
        if line in functionlist:
            b.append(line)
    return b

#returns full list with additional entries 
def findingredients(string):
    w = string.splitlines()
    z = []
    for line in w:
        if (line[0].isupper() == True) or line in functionlist:
            w.remove(line)
    for line in w:
        if (len(line) > 2) == True:
            z.append(line)
    return z

#prints units with one missing because there is one missing in pdf 
def findunits(string):
    e = findingredients(string)
    f = []
    for line in e:
        matches = [x for x in unitslist if x in line]
        if (len(matches) != 0) == True:
            f.append(matches)
    return f

    
#prints amounts with one missing because one amount not there in pdf
def findamounts(string):
    g = findingredients(string)
    h = []
    for i in range(len(g)):
        y = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', g[i])
        if (len(y) != 0) == True:
            h.append(y)
    return h 

print(findamounts(p_text))
print(len(findamounts(p_text)))
