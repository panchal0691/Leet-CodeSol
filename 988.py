class Solution:
    def __init__(self):
        self.result = ""
    
    def solve(self, root, curr):
        if not root:
            return
        
        curr = chr(root.val + ord('a')) + curr
        
        if not root.left and not root.right:
            if not self.result or self.result > curr:
                self.result = curr
            return
        
        self.solve(root.left, curr)
        self.solve(root.right, curr)
    
    def smallestFromLeaf(self, root):
        self.solve(root, "")
        return self.result
