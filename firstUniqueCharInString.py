'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

#O(N*M) O(M) space

def firstUniqChar(s): 
    dic = {} 
    for i,char in enumerate(s): 
        if char in dic: 
            dic[char] = -1 
        else: 
            dic[char] = i 
    res = float('inf') 
    for key, val in dic.items(): 
        if val == -1: 
            continue 
        res = min(res, val) 
    return res if res != float('inf') else -1

def firstUniqChar1(s): 
    dic = {} 
    res = [] 

    for index, item in enumerate(s): 
        if item not in dic: 
            dic[item] = index
            res.append(item)
        else: 
            if item in res:  
                res.remove(item)
    return dic[res[0]] if res else -1
      
        
s = "loveleetcode" #2
print(firstUniqChar(s))
print(firstUniqChar1(s))