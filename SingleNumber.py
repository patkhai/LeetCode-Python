'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

''' 

#O(n)

def singleNumber(s): 
    seen = set() 
    
    for i in s: 
        if i not in seen: 
            seen.add(i)
        else: 
            seen.remove(i)
    return str(seen).replace("{","").replace("}","")

def singleNumber2(s): 
    a = 0 
    
    for i in s: 
        a ^= i 
    return a 

s = [4,1,2,1,2]
print(singleNumber(s))
print(singleNumber2(s))