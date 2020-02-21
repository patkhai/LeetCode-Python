'''
varaible previous to store the number being replaced.


Complexity Analysis

Time complexity : O( n∗k)
Space complexity : O(1)
'''


def rotate(nums, k):
    for _ in range(k):
        previous = nums[-1] #initiate a first previous 
        for i in range(len(nums)):
            temp = nums[i] #hodl nums[i]
            nums[i] = previous #overwrite the current index 
            previous = temp #swap the value 
    return nums

print(rotate([1,2,3,4,5,6,7],3))




'''
Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

 we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest n-kn−kelements gives us the required resul

Time complexity : O(n)
Space complexity : O(1)

'''

def reverse(nums, start, end):
    while start < end: #
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1

def rotate1(nums, k):
    k %= len(nums)
    reverse(nums,0,len(nums)-1)
    reverse(nums,0, k-1)
    reverse(nums,k, len(nums)-1)
    return nums

print(rotate1([1,2,3,4,5,6,7],3))