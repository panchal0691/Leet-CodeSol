class Solution:
    def deleteNode(self, node):
        prev = None
        
        while node and node.next:
            node.val = node.next.val
            prev = node
            node = node.next
        
        del node
        if prev:
            prev.next = None
