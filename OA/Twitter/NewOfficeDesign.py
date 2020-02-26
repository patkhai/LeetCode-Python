

'''

employee table = heigts from tableheights 
holder = can hold on hastag 
heigt of hashtag is n of chars in it 

n = 4 , talbePos = [1,2,4,7], tablehe = [4,5,7,11]
  gap/space          0 1 2                0 1 3
holder count           1 

can check if they have same heign 
maxH 
minH  

3 - len(tablePos)
1
3
7
3 - len(tableHeights)
4
3
3

new office design 

''' 
def getMax(pos, height, height2):
    maxH = max(height, height2)
    minH = min(height, height2)
    
    if pos == 0:
        return 0 
    if pos == 1: 
        return minH + 1 

    if minH == maxH: 
        add = pos//2 if (pos%2 == 0) else pos//2+1
        return minH + add 

    delta = maxH - minH
    
    if delta < pos: 
        pos -= delta
        minH += delta 
        add = pos//2 if (pos%2 == 0) else pos//2+1
        return minH + add
    return minH+pos

def maxHeight(tablePositions, tableHeights):
    if tablePositions == None or tableHeights == None or len(tablePositions) != len(tableHeights): 
        return 0 

    res = 0 

    for i in range(1, len(tablePositions)): 
        currMax = getMax(tablePositions[i]-tablePositions[i-1]-1, tableHeights[i], tableHeights[i-1])
        res = max(res, currMax)
    return res 
     
    
print(maxHeight([1,3,7],[4,3,3])) # 5 

  
print(maxHeight([1,10],[1,5])) # 7 
