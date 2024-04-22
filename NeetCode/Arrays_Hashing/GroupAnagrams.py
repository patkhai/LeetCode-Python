# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


def groupAnagrams(strs):
    anagram_groups = {}
    
    for word in strs:
        # Initialize a tuple to store character counts.
        char_counts = [0] * 26  # Assuming lowercase English letters only
        
        # Count the characters in the word.
        for char in word:
            char_counts[ord(char) - ord('a')] += 1
        
        # Convert the tuple to a hashable key.
        key = tuple(char_counts)
        
        # Check if the key is already in the dictionary.
        # If not, create a new list for this group of anagrams.
        if key not in anagram_groups:
            anagram_groups[key] = []
        
        # Append the original word to the corresponding anagram group.
        anagram_groups[key].append(word)
    
    return list(anagram_groups.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)

