class Solution:
    def __init__(self):
        self.n = 0

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def backtrack(self, s, idx, curr, result):
        if idx == self.n:
            result.append(curr[:])
            return

        for i in range(idx, self.n):
            if self.isPalindrome(s, idx, i):
                curr.append(s[idx:i+1])
                self.backtrack(s, i + 1, curr, result)
                curr.pop()

    def partition(self, s):
        self.n = len(s)
        result = []
        curr = []
        self.backtrack(s, 0, curr, result)
        return result
