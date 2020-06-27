def isHappy(n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1

print(isHappy(19))#true

''' 
listset = 19 82 68 100 1  
19 
1 81
4 64
36 64
1 0 0 

'''
 