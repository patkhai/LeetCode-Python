'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 '''

 #O(n)
from collections import deque 

def maxSlidingWindow(nums, k):
    res = [] 
    queue = deque([])

    if not nums: 
        return [] 
    if k == 0: 
        return [] 

    for i, num in enumerate(nums): 
        print(i,num)
        if queue and queue[0][0] <= i - k: 
            queue.popleft() 
        while queue and queue[-1][1] < num: 
            queue.pop() 
        queue.append((i,num))
        if i >= k -1: 
            res.append(queue[0][1])
    return res 


nums = [1,3,-1,-3,5,3,6,7]
k = 3 

print(maxSlidingWindow(nums, k))