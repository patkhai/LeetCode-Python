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
        s_list = list(s)
        s_list.sort()
        key = "".join(s_list)
        if key in result_dict.keys():
            result_dict[key].append(s)
        else:
            result_dict[key] = [s]
    result = []
    for k in result_dict.keys():
        result.append(result_dict[k])
    return result

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))