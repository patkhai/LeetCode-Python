
class TreeNode: 
    def __init__(self,x): 
        self.val = x 
        self.right = None 
        self.left = None

def validBST(self, root: TreeNode): 
    stack = [] 
    curr = root 
    prev = None 

    while len(stack) or curr: 
        if curr: 
            stack.append(curr)
            curr = curr.left 
        else: 
            temp = stack.pop()
            if prev and temp.val <= prev.val: 
                return False 
            prev = temp
            curr = prev.right 
    return True 

ll = TreeNode(0)
