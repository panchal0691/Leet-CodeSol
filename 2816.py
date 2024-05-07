class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return last
    
    def doubleIt(self, head: ListNode) -> ListNode:
        head = self.reverseList(head)
        curr = head
        prev = None
        carry = 0
        
        while curr is not None:
            new_value = curr.val * 2 + carry
            curr.val = new_value % 10
            
            if new_value >= 10:
                carry = 1
            else:
                carry = 0
            
            prev = curr
            curr = curr.next
        
        if carry != 0:
            new_head = ListNode(carry)
            prev.next = new_head
        
        return self.reverseList(head)
