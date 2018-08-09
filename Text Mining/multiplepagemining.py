import PyPDF2
import re

pdf1 = open('YieldBook2015_06.pdf', 'rb')
pdf2 = open('YieldBook2015_07.pdf', 'rb')
functionlist = ['f','h','adj','i','gr','foliar ','m','water conditioner']
unitslist = ['g/l','w/w','w/v','pH']

def extracttext(pdfFileObj):
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    p_text = pageObj.extractText()
    return(p_text)

def format_spaces(a):  #a an array
    i = 0
    while i < len(a):
        if a[i] == '+':
            if (a[i+1].isspace() == True):
                del(a[i+1])
            if (a[i-1].isspace() == True):
                del(a[i-1])
        i = i + 1
    return a

#returns the table of pesticides, functions and ingredients 
def pesticidepages(p):
    return (p.split('Active ingredient', 1)[1])

#returns pesticides, functions and ingredients in standardised format
#in 2015 there are bits cut off from the ingredient/amounts entry
def standardise(w): #w an array
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
                y = h + a
                ingredients = w[h]
                while not(w[y][0].isupper()) or (w[y].isspace() == True):
                    ingredients = ingredients + w[y]
                    print(ingredients, y)
                    y = y + 1
                z.append(ingredients)
        else:
            i = i + 1
    return z

text1 = pesticidepages(extracttext(pdf1))
text2 = extracttext(pdf2)
text = (text1 + text2).splitlines()


array2015 = format_spaces(text)
standard2015 = standardise(array2015)

#for array in standardised [[tradename],[function],[ingredients],...] form
#returns wrong  numbers for K20 because 20
#some of the amounts are separate from the ingredients... add to code after the ingredients
#to find if the amounts are separate
def separate_ingredients(array):
    i = 2
    while (i < len(array)):
        array[i] = array[i].replace(',','.')
        b = array[i].split('+',1)
        h = []
        y = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', array[i])
        matches = [x for x in unitslist if x in array[i]]
        b.append(y)
        b.append(matches)
        array[i] = b
        i = i + 3
    return (array)

print(standard2015, len(standard2015))
