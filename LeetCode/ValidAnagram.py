''' 
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

'''
def if_two_words_are_permutations(s1, s2):
    if len(s1) != len(s2):
        return False
    dic = {}
    for ch in s1:
        if ch in dic.keys():
            dic[ch] += 1
        else:
            dic[ch] = 1
    for ch in s2:
        if not ch in dic.keys():
            return False
        elif dic[ch] == 0:
            return False
        else:
            dic[ch] -= 1
    return True

#O(N), #O(n) space 


def anagram(s1,s2):
    s1 = s1.replace(" ", "") 
    s2 = s2.replace(" ", "") 
    dic = {} 
    for ch in s1: 
        if ch not in dic: 
            dic[ch] = 0 #char not in dic so set value to 0 
        dic[ch]+= 1 #count the time char val seen in dic
    
    for ch in s2: 
        if ch not in dic: 
            dic[ch] = 0 
        dic[ch] -= 1 #subtract the count from dic 
    
    for key in dic.keys(): 
        if dic[key] != 0: 
            return False 
    return True 
    
            
s = "anagram"
t = "nagaram" 
b = "[]"
c = "[1]"
print(anagram(s,t))   
print(anagram(b,c))
print(if_two_words_are_permutations(s,t))