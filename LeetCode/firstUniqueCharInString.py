'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

#O(N) O(N) space

def firstUniqChar(s): 
    dic = {}    
    for v in s: 
        if v in dic:
            dic[v] += 1
        else:
            dic[v] = 1 
            
    for i, v in enumerate(s):
        if dic[v] == 1:
            return i
    return -1 

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