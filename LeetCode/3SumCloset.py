'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

def threeSumCloset(nums,target): 
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):

        # update: ignore the duplicate numbers
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            curSum = nums[l] + nums[r] + nums[i]
            if curSum == target:
                return target
            if abs(curSum-target) < abs(result-target):
                result = curSum
            if curSum < target:
                l += 1
            else:
                r -= 1
    return result

print(threeSumCloset([-1,2,1,-4], 1))
