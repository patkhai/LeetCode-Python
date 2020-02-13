def sortedSquares(A): 
    res = [] 
    right = len(A) - 1 
    left = 0
    A=[i**2 for i in A]
    
    while left <= right:
        if A[left] <= A[right]: 
            res.append(A[right])
            right -= 1 
        else:
            res.append(A[left]) 
            left += 1 
    return res[::-1] 

print(sortedSquares([-4,-1,0,3,10])) #[0,1,9,16,100]
