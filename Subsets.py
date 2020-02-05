''' 
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]

'''

#Iteratively O(2^N) O(2^N)space
#Initialize list with empty list inside it
#For each number in input
#For each list item in result
#Append (list item + number) to result list
def subsets(nums): 
    subsets = [[]]
    for num in nums: 
        for item in range(len(subsets)): 
            subsets.append(subsets[item] + [num])
    return subsets 

s = [1,2,3]
print(subsets(s))
                       
      