class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            nonlocal res
            res = max(res, left + right)
            return max(left, right) + 1
        traverse(root)
        return res
