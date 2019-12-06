'''
Created on 1 Mar 2019

@author: ostlerr
'''
import os
from pytesseract.pytesseract import Output
from imageToText.YieldBookToData import *
import string
import configparser
from enum import Enum

class Was(Enum):
    none = 0
    initital = 1
    title = 2
    name = 3
    
def loopDocs():
    global year
    year = ""
    fileList = os.listdir(srcdocs)
    fileList.sort()
    roster = ""
    year = ""
    for idx, fname in enumerate(fileList):
        nyear = fname[0:4]
        if fname.endswith(".jpg"):
            if nyear != year:
                #processRoster() 
                year = nyear
                roster = ""
            print("processing document " + str(idx) + ", " +fname)
            
            page = getPageScan(srcdocs + "\\" + fname)
            roster = roster + "\n" +  page
            #page = re.sub(" +"," ",page).strip()
            #lines = toCorrectedLines(page)        
            #getOperations(lines)
    #processRoster()
    print(roster)        
    print('done')
    outfile.close()

class Person():
    def __init__(self):
        self.department = ""
        self.name = ""
        self.role = ""
        self.qualifications = ""

def getNames(line):
    names = []
    name = ""
    
    last = Was.none
    namebits = line.split(" ")
    for idx, bit in enumerate(namebits):
        current = 0
        if re.match(r"[A-Z]\.",bit):
            current = Was.initital
        elif re.match(r"[\w]{2,3}(\.|,)", bit):
            current = Was.title
        elif re.match(r"[A-Z]{3,}", bit):
            current = Was.name
        elif re.match(r"[a-zA-Z]{3,}", bit):
            current = Was.name
            
        if idx == 0:
            name = bit
        elif last == Was.initital and current == Was.initital:
            name = " ".join([name, bit])
        elif last == Was.initital and current == Was.name:
            name = " ".join([name, bit])
            names.append(name)
            name = ""
        elif current == Was.title:
            if len(name) > 0:
                names.append(name)
            else:
                name = bit
        elif last == Was.name and current == Was.initital:
            if len(name)>0:
                names.append(name)
            name = bit        
        else:
            name = " ".join([name, bit])
        last = current
    return names

def isDepartment(line):
    departments = ["DEPARTMENT","FIELD EXP","FARM","LIBRARY","ADMINISTRATIVE","PHOTOGRAPHY","CANTEEN","INSTRUMENT"]
    for d in departments:
        if line.find(d) > -1:
            return True
    return False

def structure():
    text = rawdata.read()
    rawlines = text.split("\n")
    department = ""
    data = []
    role = ""
    for line in rawlines:
        
        if isDepartment(line):
            department = line
        elif line.find("Head of Department") > -1:
            role = "Head of Department"
            line = line[len("Head of Department"):].strip()
        elif line.find("Scientific Staff") > -1:
            role = "Scientific Staff"
            line = line[len("Scientific Staff"):].strip()
        elif line.find("Assistant Staff") > -1:
            role = "Assistant Staff"
            line = line[len("Assistant Staff"):].strip()
        elif line.find("Temporary Worker") > -1:
            role = "Temporary Worker"
            line = line[len("Temporary Worker"):].strip()
        elif line.find("Farm Workers") > -1:
            role = "Farm Workers"
            line = line[len("Farm Workers"):].strip()
        elif line.find("Recorders") > -1:
            role = "Recorders"
            line = line[len("Recorders"):].strip()
        elif line.find("Chief Technician") > -1:
            role = "Chief Technician"
            line = line[len("Chief Technician"):].strip()        
        elif line.find("Staff") > -1:
            role = "Staff"
            line = line[len("Staff"):].strip()
        elif line.find("Foreman") > -1:
            role = "Foreman"
            line = line[len("Foreman"):].strip()
        if len(line) > 5:
            if role == "Scientific Staff" or role == "Head of Department" or role == "Temporary Workers" or role == "Temporary Worker":
                namebits = line.split(",",1)
                person = Person()
                person.department = department
                person.role = role
                person.name = namebits[0]
                #print(namebits)
                if len(namebits) == 2:
                    person.qualifications = namebits[1]
                data.append(person) 
            else:
                names = getNames(line)
                for name in names:
                    person = Person()
                    person.department = department
                    person.role = role
                    person.name = name
                    data.append(person)
        #print(department)
    for person in data:
        print("1969#" + person.name + "#" + person.role + "#" + person.department + "#" + person.qualifications)    
#config = configparser.ConfigParser()
#config.read('config.ini')
#outfile = open(config['EXPERIMENT']['outfile'], "w+", 1)
#srcdocs = config['EXPERIMENT']['srcdocs']
#strSections = config['EXPERIMENT']['sections']
#sectionsNames = strSections.split(",")
outfile = open("D:\\Work\\rothamsted-ecoinformatics\\YieldbookDatasetDrafts\\staff\\staffList.txt", "w+", 1)
rawdata = open("D:\\work\\staff\\staff.txt","r",1)
srcdocs = "D:\\work\\staff\\staff.txt"
structure()
#loopDocs()