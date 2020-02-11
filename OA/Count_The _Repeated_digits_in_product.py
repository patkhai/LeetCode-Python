'''

Given a range of numbers [l, r] and an integer q. The task is to count all such number in the given range such that any digit of the 
number does not match with any digit in its product with the given number q.

Example 1:

Input: l = 10, r = 12, q = 2
Output: 1
Explanation: 
10*2 = 20 which has 0 as same digit
12*2 = 24 which as 2 as same digit
11*2 = 22 no same digit
Example 2:

Input: l = 5, r = 15, q = 2
Output: 9


'''

#O(N^2)

def rangee(l,r,q):   
    count = 0 
    
    for num in range(l,r+1): 
        product = str(num * q)
        num_sum = str(num)
        flag = True 
        for char in num_sum:
            if char in product:
                flag = False
                break;
        if flag: 
            count += 1 
    return count  
                

print(rangee(10,12,2))
print(rangee(5,15,2))
                     
    