'''

Write a function called hamming_distance which takes as input two strings, and returns the number of characters which do not match. You may assume the two strings are the same length.

hamming_distance("GATTACA","GACTATA")
2
hamming_distance("AGCAGACCCACAA","TGCAGCGAAACGA")
6

'''

def hammingDistance(s1,s2): 
    count = 0 

    s_len = len(s1)

    for i in range(s_len): 
        if s1[i] not in s2[i]: 
            count += 1 
    return count 

print(hammingDistance("GATTACA","GACTATA"))  #2 
print(hammingDistance("ACTGTGCAATACCTAAGTGAAAGGGGTGCATAGATCATTCTTTCGTTACCTCGGGTGCTATGA",
                 "ACTCCTCTGTGTCTAAGTGAAAGGGGTGCTTGCAGGGTAATCCTTCCACCTGATACCGACTCG")) #32