class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        
        t = [0] * 26
        
        result = 0
        
        for i in range(n):
            
            curr    = ord(s[i]) - ord('a')
            left    = max(0, curr - k)
            right   = min(25, curr + k)

            longest = 0
            for j in range(left, right + 1):
                longest = max(longest, t[j])
            
            t[curr] = max(t[curr], longest + 1)
            result = max(result, t[curr])
        
        return result
