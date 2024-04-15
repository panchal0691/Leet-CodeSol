class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find(self, root, curr):
        if not root:
            return 0
        
        curr = curr * 10 + root.val
        
        if not root.left and not root.right:
            return curr
        
        left_num = self.find(root.left, curr)
        right_num = self.find(root.right, curr)
        
        return left_num + right_num
    
    def sumNumbers(self, root):
        return self.find(root, 0)
