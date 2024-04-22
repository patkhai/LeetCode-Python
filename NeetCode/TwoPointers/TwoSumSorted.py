# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

def twoSumSorted(numbers, target):
    left, right = 0, len(numbers) - 1 
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target: 
            return [left+1, right+1]
        elif curr_sum < target: 
            left += 1 
        else:
            right -= 1 
    return [] 


numbers = [2,7,11,15]
target = 9
print(twoSumSorted(numbers, target))

# We initialize two pointers, left at the beginning and right at the end of the sorted array.

# We enter a while loop where we calculate the sum of the elements at numbers[left] and numbers[right].

# If the current sum is equal to the target, we return the indices left + 1 and right + 1 (1-indexed).

# If the current sum is less than the target, we increment left to move towards a larger sum.

# If the current sum is greater than the target, we decrement right to move towards a smaller sum.

# We continue this process until left is less than right.

# If no solution is found, we return an empty list.

# This algorithm runs in O(n) time complexity because each pointer moves at most once through the array, and it uses only constant extra space as required.