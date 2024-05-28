class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        
        maxLen = 0
        currCost = 0
        
        i = 0
        for j in range(n):
            currCost += abs(ord(s[j]) - ord(t[j]))
            
            while currCost > maxCost:
                currCost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            
            maxLen = max(maxLen, j - i + 1)
        
        return maxLen
