class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, small, big):
            if not node:
                return big - small
            small = min(small, node.val)
            big = max(big, node.val)
            left = dfs(node.left, small, big)
            right = dfs(node.right, small, big)
            return max(left, right)
        return dfs(root, root.val, root.val)
        #time O(n)
        #space O(n)
