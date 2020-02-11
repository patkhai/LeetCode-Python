''' 

Given a static-sized array of integers arr, move all zeroes in the array to the end of the array. You should preserve the relative order of items in the array.

We should implement a solution that is more efficient than a naive brute force.

Examples:

input:  arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
output: [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]


'''


def moveZerosToEnd(arr):
    l = len(arr)
    count = 0 
  
    for i in range(l): 
      if arr[i] != 0:
        arr[count], arr[i] = arr[i], arr[count] #swap function 
        count += 1 
        
    return arr 

print(moveZerosToEnd([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))


def moveZerosToEnd2(arr):
    length = len(arr)
    count = 0 
  
    for i in range(length): 
      if arr[i] != 0:
        arr[count] = arr[i] 
        count += 1 

    while count < length: 
        arr[count] = 0
        count += 1 
        
    return arr

print(moveZerosToEnd2([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))
