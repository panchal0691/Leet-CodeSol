class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefix_sum = 0
        mp = {}

        dummy = ListNode(0)
        dummy.next = head
        mp[0] = dummy

        while head:
            prefix_sum += head.val

            if prefix_sum in mp:
                p = mp[prefix_sum]
                start = p
                p_sum = prefix_sum

                while start != head:
                    start = start.next
                    p_sum += start.val
                    if start != head:
                        del mp[p_sum]

                p.next = start.next

            else:
                mp[prefix_sum] = head

            head = head.next

        return dummy.next

# Example usage:
# Define your linked list
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(-3)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(1)

# solution = Solution()
# result = solution.removeZeroSumSublists(head)
# while result:
#     print(result.val)
#     result = result.next
