"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        sentinel = Node(-1,head)
        current = sentinel

        lookup = {}
        def getNodeCopy(node):
            if node is None:
                return None
            if node in lookup:
                return lookup[node]

            copy = Node(node.val)
            lookup[node] = copy
            return copy

        newHead = Node(-1)
        newCurrent = newHead

        while current is not None:
            newCurrent.next = getNodeCopy(current.next)
            newCurrent.random = getNodeCopy(current.random)

            current = current.next
            newCurrent = newCurrent.next

        return newHead.next


            
        
