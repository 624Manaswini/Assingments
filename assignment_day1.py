D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
#1st

"""
D_UNION = D1 | D2
#or
#D_UNION = {**D1,**D2}
print(D_UNION)
"""
#2nd 

"""
D_intersection ={}
for k,v in D1.items():
    if k in D2:
        D_intersection[k] = v
print(D_intersection)
"""       
#3rd
"""
D_MERGE = D2.copy() 

for k,v in D1.items():
    if k in D2:  
        D_MERGE[k] = v + D2[k]
    else:
        D_MERGE[k] = v
print(D_MERGE)
"""
#4rd
"""
difference ={}
for k,v in D1.items():
    if k not in D2:
        difference[k] = v
print(difference)
"""
