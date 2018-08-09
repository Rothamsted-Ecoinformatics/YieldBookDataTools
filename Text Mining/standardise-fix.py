import PyPDF2

pdfFileObj = open('YieldBook2016_Part7.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
p_text = pageObj.extractText()
functionlist = ['f','h','adj','i','gr','foliar ','m','water conditioner']
unitslist = ['g/l','w/w','w/v','pH']

#doesnt take into account amounts and units being in differennt lines 
def standardise(string):
    w = string.splitlines()
    z = []
    i = 1
    while (i < len(w)):
        if (w[i][0].isupper() == True):
            tradename = w[i]
            j = 1
            while (w[i+j].isspace() == False):
                tradename = tradename + w[i+j]
                j = j + 1
            i = i + j
            if not any(word in tradename for word in unitslist):
                z.append(tradename)
                k = 2
                function = w[i+1]
                while (w[i+k].isspace() == False):
                    function = function + w[i+k]
                    k = k + 1
                z.append(function)
                h = i + k + 1
                a = 1
                ingredients = w[h]
                while (w[h+a].isspace() == False):
                    ingredients = ingredients + w[h+a]
                    a = a + 1
                z.append(ingredients)
        else:
            i = i + 1
    return z


print(standardise(p_text), len(standardise(p_text)))
