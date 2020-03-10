
'''
Solution: The idea of the problem is very simple and clear. You only need to count the XOR of the two int variables.
1.Exclusive OR operation
2.Count operation, can be quickly shifted by sum & (sum-1)

'''


def hammingDistance(x,y): 
    xOr_sum = x ^ y 
    count = 0 

    while xOr_sum: 
        count += 1 
        xOr_sum &= xOr_sum - 1 
    return count 

print(hammingDistance(1,4)) #2