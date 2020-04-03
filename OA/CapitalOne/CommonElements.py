'''

Find the common occurence and the values of the two arrays

'''




def commonElement(s1,s2): 

    seen = set() 
    #count = 0 
    res = [] 

    for s in s1: 
        if s not in seen: 
            seen.add(s)

    for s in seen: 
        if s in s2: 
            res.append(s)
            # count += 1 
    return res   
    

s1 = [4,7,3,2]
s2 = [4,6,3,1]

print(commonElement(s1,s2))