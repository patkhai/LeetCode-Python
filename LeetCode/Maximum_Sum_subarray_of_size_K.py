'''
To calculate the sum of the next subarray, we need to slide the window ahead by one element. So to slide the window 
forward and calculate the sum of the new position of the sliding window, we need to do two things:

Subtract the element going out of the sliding window i.e., subtract the first element of the window.
Add the new element getting included in the sliding window i.e., the element coming right after the end of the window.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].


Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''


#O(N) O(1)
def maximumSumSubarray(arr, k): 
    max_sum = 0 
    window_sum = 0 
    window_start = 0 

    for window_end in range(len(arr)): 
        window_sum += arr[window_end]
        if window_end >= k - 1: 
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1 
    return max_sum

print(maximumSumSubarray([2, 1, 5, 1, 3, 2],3))
