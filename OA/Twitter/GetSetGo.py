

'''
is subset of sum problem 

arr to keep track of possible sum to made use of subset
initialis with false 

loop throug all elements 
if sum is divisible  is done return true 

store all the new encounter sum 
loop through dp tale from 1 to requiredcal 
add curr elem to which are true in dp table 

update the temp elem to dp table

bottom up  wher val of subset be true if there is a set of 0 to j-1 with requureCal equal to i else false 

get set go 

''' 

def isPossible(calCounts, requiredCals):
    n = len(calCounts)
    subset=([[False for i in range(requiredCals+1)]  
            for i in range(n+1)]) 
       
    for i in range(n+1): 
        subset[i][0] = True
        for i in range(1,requiredCals+1): 
            subset[0][i]=False
               
        for i in range(1,n+1): 
            for j in range(1,requiredCals+1): 
                if j<calCounts[i-1]: 
                    subset[i][j] = subset[i-1][j] 
                if j>=calCounts[i-1]: 
                    subset[i][j] = (subset[i-1][j] or 
                                   subset[i - 1][j-calCounts[i-1]]) 
       
    return subset[n][requiredCals]
    

print(isPossible([2,3,15,1,16], 8)) #False 