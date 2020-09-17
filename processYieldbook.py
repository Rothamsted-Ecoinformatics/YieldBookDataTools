import csv
import os
import xmltodict

fileList = os.listdir("D:\\Work\\rothamsted-ecoinformatics\\yieldbooks\\")
fileList.sort()

with open("D:\\Work\\rothamsted-ecoinformatics\\yieldbooks\\2000.csv", "w", newline="") as csvfile:
    fieldnames = ["year","experiment_id","title","objective","sponsors","year","plot dimensions","design","treatments","basal applications","cultivations"]
    csvwriter = csv.DictWriter(csvfile, delimiter=",",quotechar="\"", quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
    csvwriter.writeheader()

    for fname in fileList:
        print("fname: " + fname)
        if fname.endswith(".xml"):
            with open("D:\\Work\\rothamsted-ecoinformatics\\yieldbooks\\" + fname) as fd:
                doc = xmltodict.parse(fd.read())
                year = fname.split(".")
                for rep in doc["experiments"]["experiment"]:
                
                    lines = rep.split("\n")
                    print(lines[0])
                    record = {}
                    counter = 0
                    title = ""
                    objective = ""
                    sponsors = ""
                    

                    s_object = rep.find("Object:")
                    s_sponsor = rep.find("Sponsor:")
                    s_design = rep.find("Design:")
                    s_treatments = rep.find("Treatments:")
                    s_basal = rep.find("Basal applications")
                    s_prev_years = rep.find("For previous years")
                    s_whole_plot = rep.find("Whole plot dimensions")
                    if s_whole_plot = rep.find("Plot dimensions")
                    
                    s_start = rep[0:s_object]
                    sp_start = s_start.split("\n")
                    record["year"] = year[0]
                    record["experiment_id"] = sp_start[0].strip()
                    record["title"] = " ".join(sp_start[1:]).strip()
                    if s_sponsor > 0:
                        record["objective"] = rep[s_object+8:s_sponsor].replace("\n"," ").strip()
                    elif s_prev_years > 0:
                        record["objective"] = rep[s_object+8:s_prev_years].replace("\n"," ").strip()
                    elif s_design > 0:
                        record["objective"] = rep[s_object+8:design].replace("\n"," ").strip()    

                    if s_sponsor > 0:
                        record["sponsors"] = rep[s_sponsor+9:s_design].replace("\n"," ").strip() 
                        #split on The   

                    if s_design > 0:
                        record["design"] = rep[s_design+7:s_whole_plot].replace("\n"," ").strip()

                    if s_whole_plot > 0:
                        record["plot dimensions"] = rep[s_whole_plot+7:s_treatments].replace("\n"," ").strip()  

                      
                    csvwriter.writerow(record)    