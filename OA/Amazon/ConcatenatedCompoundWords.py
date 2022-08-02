'''

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

return a list of lists of words which are being concatenated, 
e.g., if the input is ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"], 
the output supposed to be [["cats", "dog", "cats"], ["dog", "cats", "dog"], ["rat", "cat", "dog", "cat"].


'''

def findAllConcatenatedWordsInADict(words):
        if not words:   
            return words
        ans = []
        
        seen = set()
        
        def dfs(word):
            if not word:    return []
            if word in seen:    return [word]
            for i in range(1, len(word)):
                li = dfs(word[i:])
                if word[:i] in seen and li:
                    return li + [word[:i]]
            return []
        
        
        words.sort(key=lambda x:len(x))
        for word in words:
            li = dfs(word)
            if li:
                ans += [li]
            seen.add(word)
        return ans
       
#INPUT: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#OUTPUT:[["dog","cats","dog"],["cats","dog","cats"],["cat","dog","cat","rat"]]