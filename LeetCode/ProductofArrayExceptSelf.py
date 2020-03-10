'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

'''
#O(N) O(1)


def productExceptSelf(nums): 
    l = len(nums)
    output = [0]*l 
    output[0] = 1 

    for i in range(1,l): 
        output[i] = output[i-1] * nums[i-1]
    
    right = 1 
    for i in range(l-1,-1,-1): 
        output[i] *= right
        right *= nums[i]
    return output

print(productExceptSelf([1,2,3,4]))