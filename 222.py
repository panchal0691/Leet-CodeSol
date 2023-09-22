class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
    
        count = left + right +1
        return count
