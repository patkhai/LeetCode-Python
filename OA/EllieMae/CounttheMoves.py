'''

Given an array A[], write a function that segregates even and odd numbers. The functions should put all even numbers first, and then odd numbers.
return number of swap moves

'''


def moves(a):
    swap = -1 
    # swap = 0
    # left = 0 
    # right = len(a)-1
    # while left < right: 
    #     while(a[left] % 2 == 0): 
    #         left += 1 
    #     while(a[right] % 2 == 1): 
    #         right -= 1 
    #     if (left < right): 
    #         a[left],a[right] = a[right], a[left]
    #         left += 1
    #         right -= 1 
    #         swap += 1 
    # return swap  

    for i in range(0,len(a)): 
        if a[i] % 2 != 0: 
            swap += 1
            a[i], a[swap] = a[swap], a[i]
             
    return swap 

print(moves([13,10,21,20]))

# print(moves([8,5,11,4,6]))

