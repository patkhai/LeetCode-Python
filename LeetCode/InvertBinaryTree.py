# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.swapBranch(root)
        return root
    
    def swapBranch(self, root):
        if not root:
            return
        else:
            left = self.swapBranch(root.left)
            right = self.swapBranch(root.right)
            root.left = right
            root.right = left
        return root
    

    #recursive 
    def invertTreeRecursive(self,root:TreeNode) -> TreeNode: 
        if not root: 
            return None 

        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root 