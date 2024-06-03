class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        
        i = 0  # for s
        j = 0  # for t

        while i < m and j < n:
            if s[i] == t[j]:
                j += 1
            i += 1

        return n - j
