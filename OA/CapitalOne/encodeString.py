
'''
Given an array of words such as ["cat", "dog", "dog"]
and given an array of patterns such as ["a", "b", "b"]
return True if the words map to patterns
(such as cat maps to a, dog maps to b, and we return True since all patterns match)

Example:
["cat", "dog", "dog"]
["a", "b", "b"]
returns True

["hat", "mat", "kick"]
["a", "b", "a"]
returns False
'''

#O(n) #O(n) space
def encodeString(pattern,s):
    d = {}

    if len(s) != len(pattern): 
        return False
        
    for i in range(len(pattern)):
        if pattern[i] not in d.keys():
            d[pattern[i]] = s[i]
        else:
            if d[pattern[i]] != s[i]:
                return False 
    return True

    # mapp = {} 
    # reversemap = {} 

    # if len(s) != len(pattern): 
    #     return False 
    
    # for i in range(0, len(pattern)): 
    #     if pattern[i] not in mapp.keys() and s[i] not in reversemap.keys(): 
    #         mapp[pattern[i]] = s[i]
    #         reversemap[s[i]] = pattern[i]
    #     else: 
    #         if mapp[pattern[i]] != s[i] or reversemap[s[i]] != pattern[i]: 
    #             return False 
    # return True


pattern = ["a", "b", "b"]
s =["cat","dog", "dog"]
a = ["hat", "mat", "kick"]
d = ["a", "b", "a"]

print(encodeString(pattern,s)) #true 
print(encodeString(d,a)) #false 

