

'''

greedy approach 
all the left end of interval, store the largest right end 

check if the founain range overlap ten get the rightmost bound for next search 

activate fountain 
'''


def fountainActivation(a):
    if not a: 
        return 0 

    n = len(a)
    interval = list(range(n+1))
    for i, v in enumerate(a, 1): 
        interval[max(i-v,1)] = min(i + v, n)
    
    fountainNeed = 0 
    left = 1 
    right = interval[1]
    
    while right <= n: 
        nextRight = right 
        fountainNeed += 1 

        while left <= right: 
            nextRight = max(nextRight,interval[left])
            left += 1 
        if left > n: 
            break 
        right = max(nextRight, interval[left])
    return fountainNeed


print(fountainActivation([1,1,1])) # 1 

print(fountainActivation([2,0,0,0])) # 2 