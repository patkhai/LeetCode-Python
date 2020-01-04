#O(n)
def lengthOfLongestSubstring(s):
    length = 0 
    subString = ''
    for char in s:
        if char not in subString: 
            subString += char
            length = max(length, len(subString)) 
        else: 
            cut = subString.index(char) + 1  
            subString = subString[cut:] + char #store in the substring of the next index
    return length 
  
  
s = "abcabcbb"
a = "pwwkew" #return 3 = wke
print(lengthOfLongestSubstring(a))

'''
loop through char in the string given 
if char not in the variable substring
    add the char into the substring 
    then get the max length of the substring 
else 
    get the NEXT index of the char of that substring
    and set it to substring index's starting from that point of the index and add the charact of string 
return the length 
''' 