class Solution:
    def __init__(self):
        self.t = [[-1] * 101 for _ in range(101)]

    def solve(self, idx, open_count, s, n):
        if idx == n:
            return open_count == 0

        if self.t[idx][open_count] != -1:
            return self.t[idx][open_count] == 1

        isValid = False

        if s[idx] == '*':
            if open_count > 0:
                isValid |= self.solve(idx + 1, open_count - 1, s, n)  # Treating * as )
            isValid |= self.solve(idx + 1, open_count + 1, s, n)  # Treating * as (
            isValid |= self.solve(idx + 1, open_count, s, n)  # Treating * as ''
        elif s[idx] == '(':
            isValid |= self.solve(idx + 1, open_count + 1, s, n)
        elif open_count > 0:
            isValid |= self.solve(idx + 1, open_count - 1, s, n)

        self.t[idx][open_count] = int(isValid)
        return isValid

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        self.t = [[-1] * 101 for _ in range(101)]
        return self.solve(0, 0, s, n)
        
