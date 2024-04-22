# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 
# Time : O(nlogk)
# Space : O(n)
import heapq
from collections import Counter

# def topKFrequent(nums,k):
#     counter = Counter(nums)
#     heap = []

#     for key, val in counter.items():
#         if len(heap) < k:
#             heapq.heappush(heap,(val, key))
#         else:
#             heapq.heappushpop(heap,(val,key))
#     return [h[1] for h in heap]

# Time : O(n)
# Space : O(n)
def topKFreq(nums,k):
    n = len(nums)
    counter = Counter(nums)
    buckets = [0] * (n+1)
    
    for num, freq in counter.items():
        if buckets[freq] == 0:
            buckets[freq] = [num]
        else:
            buckets[freq].append(num)

    res = [] 
    for i in range(n, -1, -1):
        if buckets[i] != 0:
            res.extend(buckets[i])
        if len(res) == k:
            break 
    return res

# Initialize Variables:

# n = len(nums): Get the length of the input list nums.
# counter = Counter(nums): Create a counter object to count the frequency of each element in nums.
# buckets = [0] * (n+1): Initialize a list of buckets, where each bucket will hold elements with the same frequency. The index of the bucket corresponds to the frequency of elements it holds.
# Group Elements into Buckets:

# Iterate through each key-value pair in the counter.
# If the bucket for the current frequency is empty (buckets[freq] == 0), initialize it with a list containing the current element.
# Otherwise, append the current element to the existing bucket for that frequency.
# Retrieve Top k Elements:

# Iterate over the buckets in reverse order (from highest frequency to lowest).
# For each non-empty bucket encountered:
# Extend the result list res with the elements in that bucket.
# If the size of res becomes equal to k, break out of the loop since we have found the top k frequent elements.
# Return Result:

# res contains the top k frequent elements, so it is returned as the final result.

nums = [1,1,1,2,2,3]
k = 2

# print(topKFrequent(nums,k))
print(topKFreq(nums,k))