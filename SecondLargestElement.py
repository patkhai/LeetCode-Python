'''
This element becomes the secondLargest if it does not beat
the firstLargest BUT it beats the secondLargest AND is NOT
the same as the firstLargest item (so we don't unnecessarily
eject the secondLargest value if this item IS the same as the
firstLargest value)
'''


#O(N) O(1)

def secondLargest(nums):
    firstMax = float('-inf')
    secondMax = float('-inf')

    for i in range(len(nums)): 
        if nums[i] > firstMax: 
            secondMax = firstMax 
            firstMax = nums[i]
        elif nums[i] != firstMax and nums[i] > secondMax: 
            secondMax = nums[i]
    return secondMax 
        
        


print(secondLargest([1,4,5,9,2,3,8]))