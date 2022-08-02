'''

Find the longest common word in the list of words. Words are delimited by multiple spaces.
Input: ["Echo", "Alexa", "Kindle", "Echo Show", "Amazon"]
Output: "Echo"

Input: ["Echo Show", "Echo Show 8"]
Output: "Echo Show"

If there are multiple longest common words, return an empty string. 
If there is no common word, return an empty string.

'''
def logestWord(words):
    word_dict = {}
    for word in words:
        h = word.split()
        for i in h:
            if i in word_dict:
                word_dict[i] +=1
            else:
                word_dict[i] = 1
    return max(word_dict, key=word_dict.get)

logestWord(["Echo", "Alexa", "Kindle", "Echo Show", "Amazon"])