
def findMiniNumber(num): 
    mini = num[0]
    for n in range(len(num)): 
        if n < mini: 
            mini = n 
    return mini
    
n = [2,4,1,5,0,7]

print(findMiniNumber(n))