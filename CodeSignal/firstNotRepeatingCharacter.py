'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.

'''


#O(n) O(n)
def firstNotRepeatingCharacter(s):
    for c in s:
        if s.index(c) == s.rindex(c): #rindex start from last index
            return c
    return '_'


def firstNotRepeatingCharacter1(s):
    dic = {} 
    char_order = []

    for i in s: 
        if i in dic: 
            dic[i] += 1 
        else: 
            dic[i] = 1 
            char_order.append(i)
    
    for c in char_order:
      if dic[c] == 1:
        return c 
    return '_' 

print(firstNotRepeatingCharacter("aabbcde")) # c
print(firstNotRepeatingCharacter1("abcdefghijklmnopqrstuvwxyziflskecznslkjfabe")) # d