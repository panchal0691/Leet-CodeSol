from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        que = deque()

        for i in range(n):
            que.append(i)

        time = 0

        while que:
            time += 1
            front = que.popleft()
            tickets[front] -= 1

            if k == front and tickets[front] == 0:
                return time
            if tickets[front] != 0:
                que.append(front)

        return time

        
