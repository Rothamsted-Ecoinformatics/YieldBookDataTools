import PyPDF2
import re

pdfFileObj = open('YieldBook2016_Part7.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
p_text = pageObj.extractText()
functionlist = ['f','h','adj','i','gr','foliar ','m','water conditioner']
unitslist = ['g/l','w/w','w/v']

#returns full list with additional entries, without things in brackets
#some still there because the fall into different lines
def findingredients(string):
    w = string.splitlines()
    z = []
    y=[]
    for line in w:
        if (line[0].isupper() == True) or line in functionlist:
            w.remove(line)
    for line in w:
        if (len(line) > 2) == True:
            z.append(line)
    for i in range(len(z)):
        u = re.sub("[\(\[].*?[\)\]]", "", z[i])
        y.append(u)
    return y


print(findingredients(p_text))
print(len(findingredients(p_text)))
