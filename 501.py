approach one 
from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        mode_dict = defaultdict(int)  # Dictionary to store frequency of each value
        stack = []
        current = root
        max_count = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            mode_dict[current.val] += 1
            max_count = max(max_count, mode_dict[current.val])
            current = current.right

        mode = [key for key, value in mode_dict.items() if value == max_count]
        return mode


//approach two 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        best = []
        best_count = -1

        current_node = root
        current_count = 0

        def inorder(node):
            if node is None:
                return 

            inorder(node.left)
            nonlocal best 
            nonlocal best_count
            nonlocal current_node
            nonlocal current_count

            if current_node.val == node.val:
                current_count +=1
            else:
                current_node = node
                current_count =1
            if current_count > best_count:
                best = [current_node.val]
                best_count = current_count
            elif current_count == best_count:
                best.append(current_node.val)
            inorder(node.right)

        inorder(root)

        return best



Code Description:
- The code finds the mode (most frequent value) in a binary search tree.
- It performs an in-order traversal of the tree using an iterative approach and counts the frequency of each value.
- It keeps track of the value with the highest frequency (mode) and returns it.
- Time Complexity: O(N) (where N is the number of nodes in the tree).
- Space Complexity: O(N) in the worst case.
