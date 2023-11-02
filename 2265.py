# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if node is None:
                return (0,0,0)

            s1, c1, cn1 = traverse(node.left)
            s2, c2 , cn2 = traverse(node.right)

            sn , cn = s1 + s2 + node.val, c1 +c2 +1
            return (sn , cn, cn1 + cn2 + ((sn //cn) == (node.val)))

        _,_, ans = traverse(root)
        return ans
        
