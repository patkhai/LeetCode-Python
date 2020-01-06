#O(n^3), space O(1)
def longestPalindromeSubstring(s): 
   substring = '' 
   for i in range(len(s)): 
       for j in range(i+len(substring), len(s)): 
           if s[i:j+1] == s[i:j+1][::-1]: 
               if len(s[i:j+1]) > len(substring): 
                   substring = s[i:j+1]
   return substring

s = "babad" #return "bab" 
d = "cbbd" #return "bb" 
print (longestPalindromeSubstring(s)) 
print (longestPalindromeSubstring(d)) 

''' 
set var to store the strings that have met palindorme 
loop through the string, loop through the next element of the string
check if the next two string element of the(eg. 'abc'), bc = j+1, is the palindorme and also
check the reverse of that string is cba is the palindorme. 
if so check if the len of the string is greater than the substring length, therefore set the substring to that. 
return the substring 
''' 
 


