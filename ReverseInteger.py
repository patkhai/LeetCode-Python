'''
Given a 32-bit signed integer, reverse digits of an integer.

Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21

Input: 2**31 - 1 
Output: 0 

''' 

# O(log(x)), space O(1)

def reverse(x):
    reverse = 0 
    negative = x < 0 
    
    if negative: 
        x *= -1 
    
    while x > 0: 
        reverse *= 10 #push
        reverse += x % 10 #push and pop (x%10) 
        x //= 10 # continue pop operation
    
    if negative: 
        reverse *= -1
    
    if reverse > 2**31-1 or reverse < -2**31: 
        return 0 
    
    return reverse 


print(reverse(123)) # 321
print(reverse(-123)) # -321
print(reverse(-2147483648)) # 0
print(reverse(2147483647)) # 0
