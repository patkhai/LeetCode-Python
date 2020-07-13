'''
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
#O(logn)
def searchInsert(nums, target): 
    low, high = 0, len(nums)-1
    while low <= high: 
        mid = (low+high)//2
        if nums[mid] == target: 
            return mid 
        if target > nums[mid]: 
            low = mid + 1 
        else: 
            high = mid - 1 
    return low 

n = [1,3,5,6]
t = 7 
print(searchInsert(n,7)) #4 