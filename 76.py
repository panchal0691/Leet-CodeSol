from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        mp = defaultdict(int)
        
        for ch in t:
            mp[ch] += 1
        
        required_count = len(t)
        i, j = 0, 0
        min_start = 0
        min_window = float('inf')
        
        while j < n:
            ch_j = s[j]
            if mp[ch_j] > 0:
                required_count -= 1
            
            mp[ch_j] -= 1
            
            while required_count == 0:  # try to shrink the window
                if min_window > j - i + 1:
                    min_window = j - i + 1
                    min_start = i
                
                ch_i = s[i]
                mp[ch_i] += 1
                if mp[ch_i] > 0:
                    required_count += 1
                i += 1
            
            j += 1  # Don't ever forget this :-)
        
        return s[min_start:min_start + min_window] if min_window != float('inf') else ""

        
