class Solution:
    def evaluateTree(self, root):
        if not root.left and not root.right:
            return root.val
        
        if root.val == 2:
            return self.evaluateTree(root.left) | self.evaluateTree(root.right)
        
        return self.evaluateTree(root.left) & self.evaluateTree(root.right)
