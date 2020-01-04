def binarySearch(nums, target):     
    left, right = 0,len(nums) - 1 
    while left <= right: 
        mid = (left + right) // 2
        if target == nums[mid]: 
            return mid 
        elif nums[mid] > target:  #if mid point value is larger than target
            right = mid - 1 # search left
        else: 
            left = mid + 1 # search right if value is smaller 
    return -1   

n = [-1,0,3,5,9,12]
target = 9
# 9 exits in nums and its index is 4 
print(binarySearch(n,target))

''' 
binary search = check left and right and then the mid point (pivot)

while left is less than equal to right 
define mid point 
if target is equal to the mid point of the nums list at that index 
return mid point 
if mid point of the list is smaller than target value , search right side 
if mid point of the list is larger than target value , search left side 

'''