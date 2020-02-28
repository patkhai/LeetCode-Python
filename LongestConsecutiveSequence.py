'''

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''

#O(n) O(N)
#hashset
def longestConsecutive(nums):
    longest_streak = 0 
    num_set = set(nums)
    
    for num in num_set:
        if num - 1 not in num_set:
            curr = num
            curr_streak = 1 

            while curr + 1 in num_set: 
                curr += 1 
                curr_streak += 1 

            longest_streak = max(longest_streak, curr_streak)
    return longest_streak

#dic hashmap
from collections import defaultdict
def longestConsecutive2(nums):
    m = defaultdict(int)
    if len(nums) == 0:
        return 0
    for i in nums:
        m[i] = 0
    res = float('-inf')
    for i in nums:
        if i-1 not in m:
            j = i
            while j in m:
                j+=1
            res = max(res,j-i)
    return res


print(longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
print(longestConsecutive2([100, 4, 200, 1, 3, 2]))