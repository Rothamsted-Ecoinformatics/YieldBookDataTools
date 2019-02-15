'''
Created on 13 Feb 2019

@author: ostlerr
'''
from requests import get, utils
import json
from string import printable
import configparser
def uniqueWords(sentence):
    punc = "!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~"
    sentence = ''.join(x for x in sentence if x in printable)
    for s in punc:
        sentence = sentence.replace(s," ")
    print (sentence)
    #tr = str.maketrans(" ", "", punctuation)
    #clean = sentence.translate([' '*len(punctuation),punctuation])
    rawSet = set(sentence.lower().split())
    newSet = []
    for v in rawSet:
        if v.isdigit() or v.isdecimal():
            pass
        elif len(v) > 3:
            print(v)
            newSet.append(v)
    print(len(newSet))
    return newSet
 
config = configparser.ConfigParser() 
config.read('config.ini')
infile = open(config['EXPERIMENT']['outfile'], "r", 1)
data = infile.read()
print (data)
print (uniqueWords(data))

query = "http://www.ebi.ac.uk/ols/api/search?ontolgy=chebi&q=" + "demeton-s-methyl"
#equery = "http://" + urllib.parse.quote(urllib.parse.quote(query)) # double encode required

headers = {
    'Accept': 'application/json',
}
response = get(query, headers=headers)
result = json.loads(response.content)
purl = result['response']['docs'][0]
print(purl)
epurl = utils.quote(utils.quote(purl,safe="")) # double encode required
print(epurl)
query = "http://www.ebi.ac.uk/ols/api/ontologies/chebi/terms/"+epurl
response = get(query, headers=headers)
result = json.loads(response.content)
print (result)



#-L http://www.ebi.ac.uk/ols/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_40036 -i -H "Accept: application/json" >> chebi40036.json