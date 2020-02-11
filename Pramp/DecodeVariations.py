'''

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

'''
#O(N), O(1)

def decodeVariations(s):
    l = len(s)
    prev1 = 1 
    prev2 = 1 

    if l == 0 or s[0] == "0": 
        return 0 

    for i in range(1, l): 
        if s[i] == "0": 
            prev1 = 0 
        if s[i-1] == "1" or s[i-1] == "2" and s[i] <= "6": 
            prev1 = prev1 + prev2
            prev2 = prev1 - prev2 
        else: 
            prev2 = prev1 
    return prev1
  
s = '1262' #3 
d = '10' #1 

print(decodeVariations(d))
