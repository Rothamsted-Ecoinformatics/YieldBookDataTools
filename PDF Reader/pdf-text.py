import PyPDF2

pdfFileObj = open('YieldBook2016_Part7.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
p_text = pageObj.extractText()

print(p_text)
