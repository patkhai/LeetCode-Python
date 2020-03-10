'''
JUMP GAME 3 

Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
Notice that you can not jump outside of the array at any time

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
'''


from collections import deque
def canReach(arr, start):
    queue = deque()
    queue.append(start)
    seen = set()

    while queue:
        idx = queue.popleft()
        seen.add(idx)

        if arr[idx] == 0:
            return True 
        new_idx = idx + arr[idx]
        if 0 <= (new_idx) < len(arr) and new_idx not in seen:
            queue.append(new_idx)
        new_idkx = idx - arr[idx]
        if 0 <= (new_idkx) < len(arr) and new_idkx not in seen:
            queue.append(new_idkx)

    return False

print(canReach([4,2,3,0,3,1,2],5))