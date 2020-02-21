#Ebay OA

def reversePairs(n): 

    res = list(map(int, str(n)))

    print(res)
    p = []
 
    for i in range(len(res)): 
        temp = res[i-1]
        if res[i] % 2 == 0: 
            res[i-1] = res[i]
            res[i] = temp 
    
    s = [str(i) for i in res] 
    
    res = int("".join(s))

    return res
print(reversePairs(124763)) # 21