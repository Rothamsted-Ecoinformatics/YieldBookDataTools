import PyPDF2

pdfFileObj = open('YieldBook2016_Part7.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
p_text = pageObj.extractText()
functionlist = ['f','h','adj','i','gr','foliar ','m','water conditioner']


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

print(findtradenames(p_text))
print(len(findtradenames(p_text)))
