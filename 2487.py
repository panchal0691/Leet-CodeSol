class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head):
        st = []
        current = head

        while current is not None:
            st.append(current)
            current = current.next

        current = st[-1]
        st.pop()
        maximum = current.val
        result_head = ListNode(maximum)

        while st:
            current = st[-1]
            st.pop()
            if current.val < maximum:
                continue
            else:
                new_node = ListNode(current.val)
                new_node.next = result_head
                result_head = new_node
                maximum = current.val

        return result_head
