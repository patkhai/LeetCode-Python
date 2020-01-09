'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.

Input: ["bella","label","roller"]
Output: ["e","l","l"]

Input: ["cool","lock","cook"]
Output: ["c","o"]

''' 
#O(n^3) 
def commonChars(A):
    check = list(A[0])
    for word in A[1:]:
        newCheck = []
        for c in word:
            if c in check:
                newCheck.append(c)
                check.remove(c)
        check = newCheck

    return check

a = ["cool","lock","cook"]
b = ["bella","label","roller"]
print(commonChars(a))
print(commonChars(b))