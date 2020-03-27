'''
Prune all-zero subtrees from a tree. Interleave the elements of a linked list (BINARY TREE PRUNING)
Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]


1. First, we need to check if the left and right subtrees of a node contain a one
2. If there is no one, return None for the subtree(means prune it)
3. If there is one, return the root for the subtree
4. This will recursively happen in postOrder traversal
5. If the root is 1, return root
6. If root is 0, and if both left tree and right tree of the root return None, then return None for that root
The process starts from the left most node which is a leaf node which is sent as root to pruneTree
If the root is 1, return root
If root is 0, and since it does not have left or right nodes, it will return None(since no 1)
Then the function checks next leaf node, and returns root or none
If both these leaf nodes returned None, and if the root is 0, then return None
But if the root is 1, then return root
The function keeps returning root or None for all the nodes of the Binary Tree
'''
#O(N)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pruneTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None

    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)

    if root.left or root.right or root.val == 1:
        return root
    else:
        return None