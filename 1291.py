from collections import deque

class Solution:
    def sequentialDigits(self, low, high):
        que = deque()
        for i in range(1, 9):
            que.append(i)

        result = []

        while que:
            temp = que.popleft()

            if low <= temp <= high:
                result.append(temp)

            last_digit = temp % 10
            if last_digit + 1 <= 9:
                que.append(temp * 10 + (last_digit + 1))

        return result
