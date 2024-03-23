class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        stack = []
        curr = head

       # Push nodes to stack
        while curr:
            stack.append(curr)
            curr = curr.next

       # Rearrange nodes
        k = len(stack) // 2
        curr = head
        while k:
            top = stack.pop()

            temp = curr.next
            curr.next = top
            top.next = temp

            curr = temp
            k -= 1

       # Terminate the new second half
        curr.next = None
        """
        Do not return anything, modify head in-place instead.
        """
        
