class Solution:
    def maxScore(self, s: str) -> int:
        best = 0
        def c(a,d):
            return sum(1 for x in a if x == d)
        for x in range(1, len(s)):
            best = max(best,c(s[:x],"0") + c(s[x:], "1"))

        return best

        
