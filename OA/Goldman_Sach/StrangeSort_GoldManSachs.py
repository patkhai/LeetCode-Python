
'''
input : 
10 - length
2
1
4
8
6
3
0
9
7
5
8 - legnth of num 
12 -> 10
02 -> 60
4 -> 2
023 -> 605
65 -> 49
83 -> 35
224 - 2
50

output: 
4
224
12
83
65
02
50
023

0 -2
1-3 
2-0 
021 - 203

'''
def strangeSort(mapping, nums):
    dic = {}
    mapVal = []  
    lenghtMap = len(mapping)
    
    for val in range(lenghtMap): 
        dic[str(mapping[val])] = str(val)  #store index 
    
    for val in nums: 
        temp = ''
        for digit in val:
            temp += dic[digit] #store it here from dic
        mapVal.append([int(temp), val])
    #sort the new list based on the value of key at each elem of list/ based on result of lmabda function  
    mapVal = sorted(mapVal, key=lambda x: (x[0])) 
    
    for val in range(len(mapVal)): 
        mapVal[val] = mapVal[val][1]
    return mapVal
    

