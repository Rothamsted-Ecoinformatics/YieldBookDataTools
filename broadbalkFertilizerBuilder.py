import os
import csv

#54	farmyard manure
#37	ammonium sulphate
#35	Superphosphate
#49	potassium sulphate
#46	sodium sulphate
#14	Magnesium sulphate
#59	sodium nitrate


#params.append({"start": "end": "cropURI":"http://aims.fao.org/aos/agrovoc/c_8412", "nutrientRate":"", "nutrientRateUnit":"", "formURI":"", "strip":"", "factor":"", "timing":"", "comment":"","fertilizerBrand":""})
strips = []

## Strip 1  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1968, "end":2000, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"41", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"41", "factor":"N4", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2020, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N4", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2000, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N4", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1996, "end":2000, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N4", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2017, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1996, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"41", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"41", "factor":"N4", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N4", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"41", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":1,"crops":crops})

## Strip 2 
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1843, "end":1884, "nutrientRate":"225", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

strips.append({"strip":2,"crops":crops})

## Strip 2.1  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1885, "end":2020, "nutrientRate":"225", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"41", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":2004, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2005, "end":2020, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N3", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N3", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":1996, "end":2004, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"", "factor":"nil", "timing":"", "comment":"FYM N2 not applied to oats","fertilizerBrand":""})
params.append({"start":2005, "end":2020, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"", "factor":"nil", "timing":"", "comment":"FYM N3 not applied to oats","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []

params.append({"start":1997, "end":2017, "nutrientRate":"225", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2004, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2005, "end":2017, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N3", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1996, "nutrientRate":"225", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"41", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1996, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"55", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"225", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"41", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

params.append({"start":1968, "end":1995, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})

strips.append({"strip":"2.1","crops":crops})

## Strip 2.2  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1885, "end":2020, "nutrientRate":"225", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":1996, "end":2017, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"", "factor":"nil", "timing":"", "comment":"FYM not applied to oats","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"", "factor":"nil", "timing":"", "comment":"FYM not applied to oats","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"225", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1996, "nutrientRate":"225", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"225", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})
params.append({"start":1968, "end":1995, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"35","fertilizerRateUnit":"t/ha","formURI":"54", "factor":"FYM", "timing":"Autumn", "comment":"","fertilizerBrand":""})

strips.append({"strip":"2.2","crops":crops})

## Strip 3  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1844, "end":2020, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"", "factor":"nil", "timing":"", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":1996, "end":2020, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"", "factor":"nil", "timing":"", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2020, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"", "factor":"nil", "timing":"", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1996, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"", "factor":"nil", "timing":"", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"", "factor":"nil", "timing":"", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"", "factor":"nil", "timing":"", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1926, "end":1995, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"", "factor":"nil", "timing":"", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":3,"crops":crops})

## Strip 4  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1898, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"", "factor":"nil", "timing":"", "comment":"Merged with strip 3 in 1899","fertilizerBrand":""})

params.append({"start":1844, "end":1851, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1844, "end":1851, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

strips.append({"strip":4,"crops":crops})

## Strip 5  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":5,"crops":crops})

## Strip 6  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1877, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1883, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1985, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1985, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":6,"crops":crops})

## Strip 7  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1877, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1883, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":7,"crops":crops})

## Strip 8  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1877, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N3", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1883, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N3", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"120", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1985, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2020, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1985, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":8,"crops":crops})

## Strip 9a  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1854, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N1*", "timing":"spring", "comment":"","fertilizerBrand":""})
params.append({"start":1855, "end":1884, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N2*", "timing":"spring", "comment":"","fertilizerBrand":""})
params.append({"start":1885, "end":1893, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N1*", "timing":"spring", "comment":"","fertilizerBrand":""})

params.append({"start":1855, "end":1893, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1855, "end":1893, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1855, "end":1893, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1855, "end":1893, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})
strips.append({"strip":"9a","crops":crops})

## Strip 9b  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1884, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N2*", "timing":"spring", "comment":"","fertilizerBrand":""})
params.append({"start":1885, "end":1893, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N1*", "timing":"spring", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})
strips.append({"strip":"9b","crops":crops})

## Strip 9  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1894, "end":1898, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N1*", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1899, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N1*", "timing":"Spring", "comment":"first dressing","fertilizerBrand":""})
params.append({"start":1899, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N1*", "timing":"Spring", "comment":"second dressing","fertilizerBrand":""})
params.append({"start":1968, "end":1985, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2020, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1985, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":9,"crops":crops})

## Strip 10  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1877, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1883, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2000, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2000, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2017, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

strips.append({"strip":10,"crops":crops})

## Strip 11  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1877, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1883, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2000, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2017, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2018, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":11,"crops":crops})

## Strip 12  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1877, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1883, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2000, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3+1", "timing":"Spring", "comment":"First split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3+1", "timing":"Spring", "comment":"Second split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3+1", "timing":"Spring", "comment":"Third split dressing","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2000, "end":2000, "nutrientRate":"450", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"", "timing":"Autumn", "comment":"One-off application","fertilizerBrand":""})
params.append({"start":2001, "end":2005, "nutrientRate":"180", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2006, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"57", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1974, "end":2000, "nutrientRate":"55", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2000, "end":2000, "nutrientRate":"60", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"", "timing":"Autumn", "comment":"One-off application","fertilizerBrand":""})
params.append({"start":2001, "end":2005, "nutrientRate":"24", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2006, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""}) 

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3+1", "timing":"Spring", "comment":"First split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2018, "end":2020, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3+1", "timing":"Spring", "comment":"Second split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3+1", "timing":"Spring", "comment":"Third split dressing","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2000, "end":2000, "nutrientRate":"450", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"", "timing":"Autumn", "comment":"One-off application","fertilizerBrand":""})
params.append({"start":2001, "end":2005, "nutrientRate":"180", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2006, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2000, "nutrientRate":"55", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2000, "end":2000, "nutrientRate":"60", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"", "timing":"Autumn", "comment":"One-off application","fertilizerBrand":""})
params.append({"start":2001, "end":2005, "nutrientRate":"24", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2006, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg2", "timing":"Autumn", "comment":"","fertilizerBrand":""}) 

crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2000, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2017, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2+3", "timing":"Spring", "comment":"First split dressing to seedbed","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2017, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2+3", "timing":"Spring", "comment":"Second split dressing post-emergence","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2000, "end":2000, "nutrientRate":"450", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"", "timing":"Autumn", "comment":"One-off application","fertilizerBrand":""})
params.append({"start":2001, "end":2005, "nutrientRate":"180", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2006, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2000, "nutrientRate":"55", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2000, "end":2000, "nutrientRate":"60", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"", "timing":"Autumn", "comment":"One-off application","fertilizerBrand":""})
params.append({"start":2001, "end":2005, "nutrientRate":"24", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2006, "end":2017, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg2", "timing":"Autumn", "comment":"","fertilizerBrand":""}) 

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"57", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1974, "end":1996, "nutrientRate":"55", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"57", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1974, "end":1978, "nutrientRate":"55", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"57", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1974, "end":1995, "nutrientRate":"55", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na*", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":12,"crops":crops})

## Strip 13  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1877, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1883, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2000, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2000, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2017, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2017, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":13,"crops":crops})

## Strip 14  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1877, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1883, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2000, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":2000, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"39", "factor":"K*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1973, "nutrientRate":"31", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"Kieserite","fertilizerBrand":""})
params.append({"start":1974, "end":2000, "nutrientRate":"30", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2000, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"39", "factor":"K*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2000, "nutrientRate":"30", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2000, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2017, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2017, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2000, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"39", "factor":"K*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2000, "nutrientRate":"30", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"31", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"Kieserite","fertilizerBrand":""})
params.append({"start":1974, "end":1996, "nutrientRate":"30", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"39", "factor":"K*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"31", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"Kieserite","fertilizerBrand":""})
params.append({"start":1974, "end":1978, "nutrientRate":"30", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":2017, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":2000, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"39", "factor":"K*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"31", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"Kieserite","fertilizerBrand":""})
params.append({"start":1974, "end":2000, "nutrientRate":"30", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg*", "timing":"Autumn", "comment":"","fertilizerBrand":""})

strips.append({"strip":14,"crops":crops})

## Strip 15a  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1872, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1872, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1872, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1872, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1872, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

strips.append({"strip":"15a","crops":crops})

## Strip 15b  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1872, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1.5", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1872, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1872, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1872, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1872, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1872, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"0.56","fertilizerRateUnit":"t/ha","formURI":"20", "factor":"C", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

strips.append({"strip":"15b","crops":crops})

## Strip 15  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1873, "end":1878, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"spring", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1883, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1984, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"240", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N5", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2020, "nutrientRate":"240", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N5", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1873, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1873, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1873, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1873, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"120", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N5", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2018, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2018, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"240", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N5", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1984, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"240", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N5", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"240", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N5", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":15,"crops":crops})

## Strip 16

crops = []
# Wheat
params = []
params.append({"start":1852, "end":1864, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N4", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1898, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N2*", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1899, "end":1967, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N2*", "timing":"Spring", "comment":"First dressing"})
params.append({"start":1899, "end":1967, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"59", "factor":"N2*", "timing":"Spring", "comment":"Second dressing"})
params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"288", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N6", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2020, "nutrientRate":"288", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N6", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1864, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1967, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1864, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1864, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1864, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1865, "end":1883, "nutrientRate":"", "nutrientRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"", "factor":"nil", "timing":"", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N6", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []

params.append({"start":1997, "end":2017, "nutrientRate":"288", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N6", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []

params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"288", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N6", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"288", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N6", "timing":"Autumn", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

params.append({"start":1968, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

strips.append({"strip":16,"crops":crops})

## Strip 17  
## ==================================================================================================================
crops = []
# Wheat
params = []
params.append({"start":2001, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+4+1", "timing":"spring", "comment":"1st split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+4+1", "timing":"spring", "comment":"2nd split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+4+1", "timing":"spring", "comment":"3rd split dressing","fertilizerBrand":"Nitram"})

params.append({"start":2001, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412", "params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+4+1", "timing":"spring", "comment":"1st split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2018, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+4+1", "timing":"spring", "comment":"2nd split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+4+1", "timing":"spring", "comment":"3rd split dressing","fertilizerBrand":"Nitram"})

params.append({"start":2001, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":2001, "end":2017, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2+4", "timing":"spring", "comment":"1st split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2017, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2+4", "timing":"spring", "comment":"2nd split dressing","fertilizerBrand":"Nitram"})

params.append({"start":2001, "end":2017, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Beans 
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2018, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

strips.append({"strip":17,"crops":crops})

## Strip 18  
## ==================================================================================================================
crops = []
# Wheat
params = []
params.append({"start":2001, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+2+1", "timing":"spring", "comment":"1st split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+2+1", "timing":"spring", "comment":"2nd split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+2+1", "timing":"spring", "comment":"3rd split dressing","fertilizerBrand":"Nitram"})

params.append({"start":2001, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412", "params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+2+1", "timing":"spring", "comment":"1st split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2018, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+2+1", "timing":"spring", "comment":"2nd split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+2+1", "timing":"spring", "comment":"3rd split dressing","fertilizerBrand":"Nitram"})

params.append({"start":2001, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":2001, "end":2017, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2+2", "timing":"spring", "comment":"1st split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2017, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2+2", "timing":"spring", "comment":"2nd split dressing","fertilizerBrand":"Nitram"})

params.append({"start":2001, "end":2017, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Beans 
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2018, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

strips.append({"strip":18,"crops":crops})

## Strip 19  
## ==================================================================================================================
crops = []
# Wheat
params = []
params.append({"start":1852, "end":1878, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1.5", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2001, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+1+1", "timing":"spring", "comment":"1st split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+1+1", "timing":"spring", "comment":"2nd split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2020, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+1+1", "timing":"spring", "comment":"3rd split dressing","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1878, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"12", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1878, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"0.56","fertilizerRateUnit":"t/ha","formURI":"50", "factor":"C", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1879, "end":1882, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"1.91","fertilizerRateUnit":"t/ha","formURI":"50", "factor":"C", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1883, "end":1940, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"2.12","fertilizerRateUnit":"t/ha","formURI":"50", "factor":"C", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1941, "end":1988, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"20", "factor":"C", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412", "params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+1+1", "timing":"spring", "comment":"1st split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+1+1", "timing":"spring", "comment":"2nd split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2018, "end":2020, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+1+1", "timing":"spring", "comment":"3rd split dressing","fertilizerBrand":"Nitram"})

params.append({"start":2001, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":2001, "end":2017, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2+1", "timing":"spring", "comment":"1st split dressing","fertilizerBrand":"Nitram"})
params.append({"start":2001, "end":2017, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N2+1", "timing":"spring", "comment":"2nd split dressing","fertilizerBrand":"Nitram"})

params.append({"start":2001, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2001, "end":2017, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1988, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"20", "factor":"C", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":2018, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"20", "factor":"C", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1878, "nutrientRate":"35", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1988, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"20", "factor":"C", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":19,"crops":crops})

## Strip 20  
## ==================================================================================================================

crops = []
# Wheat
params = []
params.append({"start":1906, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1906, "end":1967, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":2020, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1906, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1906, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1906, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412","params":params})

# Oats
params = []
params.append({"start":2018, "end":2020, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1996, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2017, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":2017, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":2017, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1996, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1996, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":2018, "end":2020, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow
params = []
params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1995, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1968, "end":1995, "nutrientRate":"90", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"16", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1995, "nutrientRate":"11", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":20,"crops":crops})

strips2 = []
## Strip 17 alternating  
## ==================================================================================================================
crops = []
# Wheat
params = []
params.append({"start":1852, "end":1876, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "formURI":"37", "factor":"N1", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1878, "end":1882, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "formURI":"37", "factor":"N1", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1966, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "formURI":"37", "factor":"N1", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1884, "end":1966, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "formURI":"37", "factor":"N1", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1985, "end":1985, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "formURI":"41", "factor":"N0+3", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"0", "nutrientRateUnit":"kgN/ha", "formURI":"55", "factor":"N0+3", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1987, "end":1999, "nutrientRate":"0", "nutrientRateUnit":"kgN/ha", "formURI":"55", "factor":"N0+3", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"autumn", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":1987, "end":1999, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "formURI":"55", "factor":"N0+3", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":1986, "end":2000, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "formURI":"55", "factor":"N1+3", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"autumn", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":1986, "end":2000, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "formURI":"55", "factor":"N1+3", "fertilizerRate":"","fertilizerRateUnit":"", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1853, "end":1967, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1985, "end":1999, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1853, "end":1967, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1985, "end":1999, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1853, "end":1967, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1853, "end":1967, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412", "params":params})

# Oats
params = []
params.append({"start":1997, "end":1999, "nutrientRate":"17.", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":1999, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":1999, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":1999, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N0+3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":1998, "end":2000, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1997, "end":1999, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":1999, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1997, "end":1999, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
#params.append({"start":1985, "end":1985, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1986, "end":1996, "nutrientRate":"192", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N4", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1985, "end":1995, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1985, "end":1995, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Fallow 
params = []

params.append({"start":1985, "end":1999, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1985, "end":1999, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips2.append({"strip":17,"crops":crops})

## Strip 18 alternating  
## ==================================================================================================================
crops = []
# Wheat
params = []
params.append({"start":1853, "end":1877, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1879, "end":1883, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1885, "end":1967, "nutrientRate":"24", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1885, "end":1967, "nutrientRate":"72", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"37", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":""})
params.append({"start":1985, "end":1985, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1+3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1985, "end":1985, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1+3", "timing":"autumn", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1987, "end":1999, "nutrientRate":"48", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3", "timing":"autumn", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":1987, "end":1999, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":1986, "end":2000, "nutrientRate":"0", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N0+3", "timing":"autumn", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":1986, "end":2000, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N0+3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1852, "end":1966, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"35", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1986, "end":2000, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1966, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})
params.append({"start":1886, "end":2000, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1966, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1852, "end":1966, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412", "params":params})

# Oats
params = []
params.append({"start":1996, "end":2000, "nutrientRate":"17.", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2000, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1996, "end":2000, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1998, "end":2000, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})
params.append({"start":1997, "end":1999, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N0+3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1998, "end":2000, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1998, "end":2000, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1998, "end":2000, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1985, "end":1985, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1+3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})
params.append({"start":1987, "end":1995, "nutrientRate":"144", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"55", "factor":"N1+3", "timing":"Spring", "comment":"","fertilizerBrand":"Nitram"})

params.append({"start":1986, "end":1996, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1986, "end":1996, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Fallow 
params = []

params.append({"start":1986, "end":2000, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1886, "end":2000, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips2.append({"strip":18,"crops":crops})

## Strip 17 1968-84  
## ==================================================================================================================
crops = []
# Wheat
params = []
params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1984, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1984, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1868, "end":1973, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1868, "end":1973, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412", "params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1984, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1984, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow 
params = []

params.append({"start":1968, "end":1978, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":17,"crops":crops})

## Strip 18 1968-84  
## ==================================================================================================================
crops = []
# Wheat
params = []
params.append({"start":1969, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1984, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1984, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412", "params":params})

# Potatoes
params = []
params.append({"start":1968, "end":1984, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N2", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1984, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1984, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1968, "end":1978, "nutrientRate":"96", "nutrientRateUnit":"kgN/ha", "fertilizerRate":"","fertilizerRateUnit":"", "formURI":"41", "factor":"N1", "timing":"Spring", "comment":"","fertilizerBrand":"Nitro-chalk"})

params.append({"start":1968, "end":1978, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1978, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1972, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1972, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow 
params = []

params.append({"start":1968, "end":1984, "nutrientRate":"17.5", "nutrientRateUnit":"kgP/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"4", "factor":"P", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1984, "nutrientRate":"45", "nutrientRateUnit":"kgK/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"49", "factor":"K", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"8", "nutrientRateUnit":"kgNa/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"46", "factor":"Na", "timing":"Autumn", "comment":"","fertilizerBrand":""})

params.append({"start":1968, "end":1973, "nutrientRate":"5.5", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":""})

crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips.append({"strip":18,"crops":crops})


# ==================================================================================================================
# Alternating Mg 1974 - 2000
# ==================================================================================================================
strips3 = []

crops = []
# Wheat
params = []
params.append({"start":1974, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":"Kieserite"})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_8412", "params":params})

# Oats
params = []
params.append({"start":1996, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":"Kieserite"})
crops.append({"crop":"http://farms.rothamsted.ac.uk/c_c0008","params":params})

# Maize
params = []
params.append({"start":1997, "end":2000, "nutrientRate":"35", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":"Kieserite"})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_12332","params":params})

# Potatoes
params = []
params.append({"start":1974, "end":1996, "nutrientRate":"35", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":"Kieserite"})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_13551","params":params})

# Beans 
params = []
params.append({"start":1974, "end":1978, "nutrientRate":"35", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":"Kieserite"})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_331566","params":params})

# Fallow 
params = []
params.append({"start":1974, "end":1995, "nutrientRate":"35", "nutrientRateUnit":"kgMg/ha", "fertilizerRate":"","fertilizerRateUnit":"","formURI":"14", "factor":"Mg", "timing":"Autumn", "comment":"","fertilizerBrand":"Kieserite"})
crops.append({"crop":"http://aims.fao.org/aos/agrovoc/c_34007","params":params})

strips3.append({"strip":5,"crops":crops})
strips3.append({"strip":6,"crops":crops})
strips3.append({"strip":7,"crops":crops})
strips3.append({"strip":8,"crops":crops})
strips3.append({"strip":9,"crops":crops})
strips3.append({"strip":15,"crops":crops})
strips3.append({"strip":16,"crops":crops})
strips3.append({"strip":20,"crops":crops})
##?strips3.append({"strip":17,"crops":crops})
##?strips3.append({"strip":18,"crops":crops})

experimentId = "R/BK/1"
activityURI = "http://aims.fao.org/aos/agrovoc/c_10795"

with open('tempFertilzerList.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for strip in strips3:
        stp = strip["strip"]
        clist = strip["crops"]
        for crop in clist:
            c = crop["crop"]
            plist = crop["params"]
            print(c)
            for p in plist:
                s = int(p["start"])
                e = int(p["end"])+1
                print(str(s) + ", " + str(e))
                factor = p["factor"]
                nutrientRate = p["nutrientRate"]
                nutrientRateUnit = p["nutrientRateUnit"]
                fertilizerRate = p["fertilizerRate"]
                fertilizerRateUnit = p["fertilizerRateUnit"]
                formURI = p["formURI"]
                timing = p["timing"]
                comment = p["comment"]
                for i in range(s,e):
                    writer.writerow([experimentId,str(i),str(s),str(e),activityURI,c,nutrientRate,nutrientRateUnit,fertilizerRate,fertilizerRateUnit,formURI,stp,factor,timing,comment])
                    i = i+3

    for strip in strips2:
        stp = strip["strip"]
        clist = strip["crops"]
        for crop in clist:
            c = crop["crop"]
            plist = crop["params"]
            print(c)
            for p in plist:
                s = int(p["start"])
                e = int(p["end"])+1
                print(str(s) + ", " + str(e))
                factor = p["factor"]
                nutrientRate = p["nutrientRate"]
                nutrientRateUnit = p["nutrientRateUnit"]
                fertilizerRate = p["fertilizerRate"]
                fertilizerRateUnit = p["fertilizerRateUnit"]
                formURI = p["formURI"]
                timing = p["timing"]
                comment = p["comment"]
                for i in range(s,e):
                    writer.writerow([experimentId,str(i),str(s),str(e),activityURI,c,nutrientRate,nutrientRateUnit,fertilizerRate,fertilizerRateUnit,formURI,stp,factor,timing,comment])
                    i = i+2

    for strip in strips:
        stp = strip["strip"]
        clist = strip["crops"]
        print(stp)
        for crop in clist:
            c = crop["crop"]
            plist = crop["params"]
            print(c)
            for p in plist:
                s = int(p["start"])
                e = int(p["end"])+1
                print(str(s) + ", " + str(e))
                factor = p["factor"]
                nutrientRate = p["nutrientRate"]
                nutrientRateUnit = p["nutrientRateUnit"]
                fertilizerRate = p["fertilizerRate"]
                fertilizerRateUnit = p["fertilizerRateUnit"]
                formURI = p["formURI"]
                timing = p["timing"]
                comment = p["comment"]
                for i in range(s,e):
                    if (i == 1915 and factor in ["P", "K", "Na", "Na*", "Mg", "Mg*"]):
                        pass
                    elif (i in [1917,1918,1919] and factor in ["C", "K", "Na*", "Mg*"]):
                        pass
                    else:
                        writer.writerow([experimentId,str(i),str(s),str(e),activityURI,c,nutrientRate,nutrientRateUnit,fertilizerRate,fertilizerRateUnit,formURI,stp,factor,timing,comment])
# strip 17 and 18 need different loops for alternating years.
