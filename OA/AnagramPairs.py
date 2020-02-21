
'''
Count the numbers of anagram pairs exit in the array of integers

''' 

#O(N)

def anagram_pairs(s) : 

    res = [str(item) for item in s]
    # To store count of strings 
    mp = dict.fromkeys(res, 0)
    # Traverse all strings and store in the map 
    for i in range(len(res)) : 
        temp_ar = list(res[i])
        # Sort the list of characters 
        temp_ar.sort()
        # make a sorted string 
        res[i] = "".join(temp_ar)
        # Store in the map 
        mp[res[i]] += 1; 
          
    # To store the number of pairs 
    ans = 0
    # Traverse through the map 
    for k in mp.values() : 
        # Count the pairs for each string 
        ans += (k * (k - 1)) // 2
    # Return the required answer 
    return ans

print(anagram_pairs([ 12, 31, 21,  
          13, 145 ])) # 2