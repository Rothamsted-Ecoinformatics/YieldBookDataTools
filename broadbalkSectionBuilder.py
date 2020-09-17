import os
import csv

sections = []

# section I (1926-1954)
sections.append({"section":"I","start":1926, "end":1954,"fallowYears":[1926,1927,1931,1936,1941,1946,1951]})

# section Ia (1955-1967) wheat only
sections.append({"section":"Ia","start":1955, "end":1967,"fallowYears":[]})

# section Ib (1955-1967) 
sections.append({"section":"Ia","start":1955, "end":1967,"fallowYears":[1956,1961,1966]})

# section II (1926-1967) 
sections.append({"section":"II","start":1926, "end":1967,"fallowYears":[1926,1927,1932,1937,1942,1947,1952,1957,1962,1967]})

# section III (1926-1967) 
sections.append({"section":"III","start":1926, "end":1967,"fallowYears":[1926,1927,1928,1929,1935,1940,1945,1950,1955,1960,1965]})

# section IV (1926-1967) 
sections.append({"section":"IV","start":1926, "end":1967,"fallowYears":[1928,1929,1934,1939,1944,1949,1954,1959,1964]})

# section V (1926-1954) 
sections.append({"section":"V","start":1926, "end":1954,"fallowYears":[1928,1929,1933,1938,1943,1948,1954]})

# section Va (1955-1967) 
sections.append({"section":"Va","start":1955, "end":1967,"fallowYears":[1958,1963]})

# section Vb (1955-1967) 
sections.append({"section":"Vb","start":1955, "end":1967,"fallowYears":[1963]})

with open('tempCroppingList.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for section in sections:
        sname = section["section"]
        fyears = section["fallowYears"]
        s = int(section["start"])
        e = int(section["end"])+1
        for n in range(s,e):
            if n in fyears:
                writer.writerow([sname,"http://aims.fao.org/aos/agrovoc/c_34007",str(n)])
            else:
                writer.writerow([sname,"http://aims.fao.org/aos/agrovoc/c_8412",str(n)])