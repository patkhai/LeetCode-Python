'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''


#O(N) 

def longestCommonPrefix(s): 
    res = ""
    # Create one iterator per string using zip, it will stop at the shortest string
    # s is a tuple of characters at current position for each string
    # create a set to test unicity
    
    for i in zip(*s): 
        if len(set(i)) != 1: 
            return res 
        res += i[0]
    return s
  
        
s = ["flower","fleet","flat"] #fl
print(longestCommonPrefix(s))