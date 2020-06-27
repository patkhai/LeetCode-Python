"""
You need to find the largest value in each row of a binary tree.
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]


   10.  
16     12
20 14   11 6 
output : [10,16,20]

if tree null, return empty 

plan: 
dfs, bfs 

pusedeo: 
  initialize dic 
  create helper fucntion 
    loop through the node, 
    check if the depth is in dic 
      if so find the max 
      if not that depth will be node val 

Time: O(N)
Space: O(logN)

"""

from typing import List

class TreeNode: 
    def __init__(self,val=0,left=None, right=None): 
        self.val = val 
        self.left = left
        self.right = right

node_3_1 = TreeNode(3)
node_5 = TreeNode(5)
node_9 = TreeNode(9)
node_3_2 = TreeNode(3)
node_2 = TreeNode(2)
node_1 = TreeNode(1)

node_3_2.left = node_5
node_3_2.right = node_3_1
node_2.right = node_9
node_1.left = node_3_2
node_1.right = node_2

def largest_values(root: TreeNode) -> List[int]: 
    def helper_dfs(node, depth): 
        if node: 
            if depth in res: 
                res[depth] = max(node.val, res[depth])
            else: 
                res[depth] = node.val 
        else: 
            return None 
        helper_dfs(node.left, depth+1)
        helper_dfs(node.right, depth+1)
    
    res = {} 
    helper_dfs(root, 0)
    return list(res.values())

print(largest_values(node_1))