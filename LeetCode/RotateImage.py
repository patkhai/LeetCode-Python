'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).
Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

def rotateImage(matrix): 
    m = len(matrix)
        
    #Transpose, symmetry swap
    for i in range(m): 
        for j in range(i): 
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
    
    #horizontal swap (m//2 for mid point) reverse 
    for i in range(m): 
        for j in range(m//2): 
            matrix[i][j], matrix[i][m-1-j] = matrix[i][m-1-j],matrix[i][j]
        
    return matrix

print(rotateImage([ 
  [1,2,3], # 1 4 7 
  [4,5,6], # 2 5 8
  [7,8,9]  # 3 6 9 
]))

print(rotateImage([
  [ 5, 1, 9,11], #5  2  13 15
  [ 2, 4, 8,10], #1  4  3  14
  [13, 3, 6, 7], #9  8  6  12 
  [15,14,12,16]  #11 10 7  16
]))