class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sum(self, curr, parent):
        if not curr:
            return 0
        
        left = self.sum(curr.left, curr)
        right = self.sum(curr.right, curr)
        
        s = 0
        if not curr.left and not curr.right:
            if parent and parent.left == curr:
                s += curr.val
        
        return left + right + s
    
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        parent = None
        return self.sum(root, parent)
