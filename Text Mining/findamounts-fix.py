import PyPDF2
import re

pdfFileObj = open('YieldBook2016_Part7.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
p_text = pageObj.extractText()
functionlist = ['f','h','adj','i','gr','foliar ','m','water conditioner']
unitslist = ['g/l','w/w','w/v']

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

#prints amounts with one missing because one amount not there in pdf
def findamounts(string):
    w = findingredients(string)
    z = []
    for i in range(len(w)):
        y = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', w[i])
        if (len(y) != 0) == True:
            z.append(y)
    return z

#re.findall('\(.*?\)',s) finds bracketed phrases

#prints units with one missing because there is one missing in pdf 
def findunits(string):
    w = findingredients(string)
    z = []
    for line in w:
        matches = [x for x in unitslist if x in line]
        if (len(matches) != 0) == True:
            z.append(matches)
    return z


print(p_text.splitlines())
