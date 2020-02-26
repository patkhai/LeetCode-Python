
'''
3 col 
2 row 
3 expirylimit value

break down the commands
    - 3 variables to keep track 
    - set the token if there is no task command 
        - expirylimimt + T
    - reset token if expires 
        - first check token exist in the dic 
            - expirtlimit + T if expiry time greater than T 
    
- keep track of the dic counted 

authentication tokens

'''

def numberOfTokens(expiryLimit, commands):
    T = 0 
    dic = {} 
    count = 0

    for seq in commands: 
        task = seq[0] 
        token_id = seq[1]
        T = seq[2]
        
        if task == 1: 
            if token_id in dic.keys(): 
                expiration = dic.get(token_id)
                if T <= expiration: 
                    dic[token_id] = T + expiryLimit
        elif task == 0:
            dic[token_id] = T + expiryLimit
    
    for i in dic.values(): 
        if i >= T:
            count += 1 
    return count

print(numberOfTokens(3,[[0,1,1],[1,1,5]])) #0 
print(numberOfTokens(3,[[0,1,1],[1,1,4],[1,2,5]])) # 1
