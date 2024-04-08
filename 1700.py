from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length = len(students)
        que = deque()
        st = []

        for i in range(length):
            st.append(sandwiches[length - i - 1])
            que.append(students[i])

        last_served = 0
        while que and last_served < len(que):
            if st[-1] == que[0]:
                st.pop()
                que.popleft()
                last_served = 0
            else:
                que.append(que[0])
                que.popleft()
                last_served += 1

        return len(que)
        
