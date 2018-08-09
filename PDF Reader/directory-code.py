import os
from PyPDF2 import PdfFileReader

fileList = os.listdir(r"\\salt\r3scans")
for fname in fileList:
    if (fname.count("YieldBook") == 1):
        print("search: " + "\\salt\\r3scans\\"+fname)
        subfiles = os.listdir(r"\\salt\\r3scans\\"+fname)
        for sfname in subfiles: 
                if (sfname.count("YieldBook") == 1):
                    print(fname+"\\"+sfname,"Y")
                else:
                    print(fname+"\\"+sfname,"N")
