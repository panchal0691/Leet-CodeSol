class Solution:
    def minSteps(self, s: str, t: str) -> int:
        n = len(s)
        
        mp_s = [0] * 26
        mp_t = [0] * 26
        
        for i in range(n):
            mp_s[ord(s[i]) - ord('a')] += 1
            mp_t[ord(t[i]) - ord('a')] += 1
        
        result = 0
        
        for i in range(26):
            freq_in_t = mp_t[i]
            freq_in_s = mp_s[i]
            
            if freq_in_t < freq_in_s:
                result += freq_in_s - freq_in_t
        
        return result
        
