'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
'''
def letterCasePermutation(S):
    ans = [""]
    for c in S:
        if c.isnumeric():
            ans = [s+c for s in ans]
        else:
            s1 =  [s+c.lower() for s in ans]
            s2 =  [s+c.upper() for s in ans]
            ans = s1 + s2
    return ans

print(letterCasePermutation("a1b2"))

