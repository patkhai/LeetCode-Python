#O(n^2)
def BruteForceTWOSUM(nums, target): 
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)): 
            sums = nums[i] + nums[j]
            if sums == target: 
                return [i,j]

#O(n)
def TwoSum(nums, target):
    dic = dict() 
    for i in range(len(nums)): 
        complement = target - nums[i] 
        if complement in dic: 
            return [dic[complement], i]
        dic[nums[i]] = i  #keep adding the cur num and index in DIC 

#O(n) with enumerate 
def TwoSum_enumerate(nums, target):
    dic = dict()
    for i, n in enumerate(nums): 
        complement = target - n 
        if complement in dic: 
            return [dic[complement], i]
        dic[n] = i  #keep adding the cur num and index in DIC 

num = [2,7,11,15]
target = 18 

#return [0,1] #indexs = 2, 7 
print(BruteForceTWOSUM(num,target))
print(TwoSum_enumerate(num,target))
print(TwoSum(num,target))


''' 
create a dict 
loop through the range and len of the num list 
get the value of the target minus first index of the num list 
if the value you get from subtracting is in the dict that you created 
    return the index from the dic and the index of the list you are in 
else just set the dic index of the num list into your index of the list you are currently in 

''' 