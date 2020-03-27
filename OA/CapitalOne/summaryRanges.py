'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''


#O(n) O(1)
def summaryRanges(nums):
    out = []
    i = 0 
    while i<len(nums): 
        start = nums[i]
        while i<len(nums)-1 and nums[i]+1==nums[i+1]:
            i+=1
        end = nums[i]
        if end==start: 
            out.append("{}".format(start))
        else: 
            out.append("{}->{}".format(start, end))
        i+=1
    return out

print(summaryRanges([0,1,2,4,5,7]))

#O(n) O(n)
def summ(nums): 
    def printRanges(start,end): 
        res = str(start)
        if start != end: 
            res += "->" + str(end) 
        return res  

    res = [] 

    if not nums: 
        return res 
    
    start = curr = None 
    for num in nums: 
        if start == None: 
            start = curr = num 
        elif num == curr + 1: 
            curr = num 
        else: 
            res.append(printRanges(start,curr))
            start = curr = num 
    res.append(printRanges(start,curr))
    return res 

 

print(summ([0,1,2,4,5,7]))