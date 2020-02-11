'''
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''

#O(N), O(1)

def sort_k_messed_array(arr,k): 
    if len(arr)<= 1 or k ==0: 
        return arr
    for i in range(1,len(arr)): 
        curr = i 
        prev = i -1
        diff = 1 
        while (curr>=0 and prev >=0) and arr[curr]<arr[prev]:
            temp = arr[curr] 
            arr[curr] = arr[prev] 
            arr[prev] = temp 
            curr-=1
            prev-=1 
            if i >= k: 
                if diff == k: 
                    break 
                diff += 1 
    return arr

print((sort_k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9],2)))