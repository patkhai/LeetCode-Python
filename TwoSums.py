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

num = [2,7,11,15]
target = 18 

#return [0,1] #indexs = 2, 7 
print(BruteForceTWOSUM(num,target))
print(TwoSum(num,target))
