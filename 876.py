# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head 
        sec = head
        while first and first.next:
            sec = sec.next
            first = first.next.next

        return sec
