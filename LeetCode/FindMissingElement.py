'''
Given two arrays which are duplicates of each other except one element, that is one element from one of the array is missing, we need to find that missing element.

Examples:

Input:  arr1[] = {1, 4, 5, 7, 9}
        arr2[] = {4, 5, 7, 9}
Output: 1
1 is missing from second array.

Input: arr1[] = {2, 3, 4, 5}
       arr2[] = {2, 3, 4, 5, 6}
Output: 6
6 is missing from first array.

'''
#O(logn) O(n)
def findMissing(A,B): 
    left = 0 
    right = len(B) - 1 

    while left < right: 
        mid = (left+right) // 2 

        if A[mid] == B[mid]: 
            left = mid 
        else: 
            right = mid 
        
        if left == right - 1: 
            break 
    return A[right]

#O(n) O(1)
def findMissing_XOR(A,B): 
    xor_sum = 0 
    for num in A: 
        xor_sum ^= num
    for num in B: 
        xor_sum ^= num 
    return xor_sum 

print(findMissing_XOR([1,24,5,7],[1,24,7]))
print(findMissing([1,24,5,7],[1,24,7]))