def numJewelsInStones(J, S):
    charToFreqS = {}  # Map character to its frequency in S.
    numJewels = 0  # Total number of jewels.
    
    for ch in S:
        if ch not in charToFreqS:
            charToFreqS[ch] = 1
        else:
            charToFreqS[ch] += 1
    
    for ch in J:
        if ch in charToFreqS:
            numJewels += charToFreqS[ch]
            
    return numJewels

def numJewelsInStones2(J,S): 
    count = 0 
    for ch in S:
        if ch in J: 
            count += 1 
    return count 

J = "aA"
S = "aAAbbbb"
# print(numJewelsInStones(J,S))
print(numJewelsInStones2(J,S))