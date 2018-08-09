import PyPDF2

pdfFileObj = open('YieldBook2016_Part6.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
p_text= pageObj.extractText()

#returns the table of pesticides, functions and ingredients 
def pesticidepages(p):
    return (p.split('Active ingredient', 1)[1])

#def findtradenames(string):
 #   w = string.splitlines()
  #  z=[]
   # for line in w:
    #    if (line[0].isupper() == True):
     #       z.append(line)
      #  for zline in z:
       #     if (len(zline) <= 2) == True:
        #        z.remove(zline)
   # return z


#print(findtradenames(pesticidepages(p_text)))


print(pesticidepages(p_text).splitlines())
