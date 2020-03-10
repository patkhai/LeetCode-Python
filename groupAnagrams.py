'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''


#O(nlogn) O(nk)
def groupAnagrams(strs):
    result_dict = {}
    
    for s in strs: 
        key = ''.join(sorted(s))

        if key not in result_dict: 
            result_dict[key] = [s]
        else: 
            result_dict[key] += [s]

    return list(result_dict.values())


print(groupAnagrams(["car", "tree", "boy", "girl", "arc"]))