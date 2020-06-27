'''
 Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

#O(N)

def isIsomorphic(s, t):
        if len(s) != len(t): 
            return False 
        
        return halfIso(s,t) and halfIso(t,s)

def halfIso(s,t): 
    lookup = {} 
    
    for i in range(len(s)): 
        if s[i] not in lookup: 
            lookup[s[i]] = t[i] 
        elif lookup[s[i]] != t[i]: 
            return False 
    return True 


s = "egg"
t = "add"


k = "foo"
p = "bar"
print(isIsomorphic(s,t)) #true 
print(isIsomorphic(k,p)) #true 
