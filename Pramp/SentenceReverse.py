"""
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't']

"""

#O(N) O(1)

def reverse_words(arr):
  s_spaces = []
  r = []
  for i in range(len(arr)): 
    if i == len(arr)-1:
      r.append(arr[i])
      s_spaces.append(r)
      r = []
    elif arr[i] == ' ' :
      s_spaces.append(r)
      r = []
    else:
      r.append(arr[i])
      
  result = []
  tail = 0
  head = len(s_spaces) - 1
  
  while tail < head:
      s_spaces[tail],s_spaces[head] = s_spaces[head],s_spaces[tail]
      tail +=1
      head -=1      
    
  for i,w in enumerate(s_spaces):
    result += w
    if i != len(s_spaces) -1:
      result.append(' ')
  return result 
  
  
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
                'm', 'a', 'k', 'e', 's', ' ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]



print(reverse_words(arr))