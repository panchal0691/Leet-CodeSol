class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root):
        if not root:
            return ""

        result = str(root.val)
        l = self.tree2str(root.left)
        r = self.tree2str(root.right)

        if not root.left and not root.right:
            return result

        if not root.right:
            return result + "(" + l + ")"

        if not root.left:
            return result + "()" + "(" + r + ")"

        return result + "(" + l + ")" + "(" + r + ")"
