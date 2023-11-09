class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9+7
        ans =0
        streak =0
        last = ""
        for c in s:
            if c == last:
                streak +=1
            else:
                streak =1
            last =c
            ans += streak
        return ans % MOD



        
