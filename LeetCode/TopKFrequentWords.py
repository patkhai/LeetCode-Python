'''
Use lambda to sort the dictionary in desc order based on words frequency and if frequency are equal then sort dictionary in asc order based on the word alphabet.
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.


'''

#O(nlogn), O(N)
def topKFrequent(words,k): 
    dict = {}
    for x in words:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    res = sorted(dict, key=lambda x: (-dict[x], x))
    return res[:k]

w = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

print(topKFrequent(w,k)) #['i', 'love']
