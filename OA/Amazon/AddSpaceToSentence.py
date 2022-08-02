'''
Add spaces to a sentence given a sentence and dictionary. "iloveamazon" should return "i love amazon" for example.

Every time, we check whether s starts with a word. If so, we check whether the substring s[len(word):] starts with a word, etc.
2.resultOfTheRest keeps calling until we hit the last word. If the last word is in the dict, we append it to res.
The last word is 'dog ==> 'res = [ "dog"]
3. This time, we skip "else," since we fulfill the condition " if len(word) == len(s)." 
We store it in memo: {'dog': ['dog']}

4.Then we return to "resultOfTheRest = self.helper(s[len(word):], wordDict, memo)"
s = "sanddog" because we start with "cat" (cat is the first word in the dict) and "cat" leads to "sand".
resultOfTheRest = ["dog"]
word = "sand"
item = "sand dog"
res = ["sand dog"]
memo ={'dog': ['dog'], "sanddog":["sand dog"] }

Why do we need memo?
We always recurse to the last word in the string and backtrack, 
so storing all possible combinations of the substring in the memo 
saves time for the next iteration of the whole string. 
For example, "catsanddog," if we don't store "dog," then we have to iterate 
through the dictionary. This is very DP.
'''


def wordBreak(s, wordDict):

    memo = {}

    def dfs(s):
        if s in memo:
            return memo[s]

        res = []
        for x in wordDict:
            if s.startswith(x):
                if s == x:
                    res += [x]
                else:
                    for y in dfs(s[len(x):]):
                        res += [x + ' ' + y]
        memo[s] = res
        return res

    return dfs(s)


s = "iloveamazon"
wordDict = ["i", "love", "amazon"]
print(wordBreak(s, wordDict))
