class Solution:
    def check(self, s, i, j):
        if i >= j:
            return True
        if s[i] == s[j]:
            return self.check(s, i+1, j-1)
        return False
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if self.check(s, i, j):
                    count += 1
        return count
        
