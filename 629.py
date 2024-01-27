class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7    
        dp = [0] * (k+1)
        dp[0] = 1
        #n dimension 
        for i in range(1, n + 1):
            new_dp = [0] * (k+1)
            #sliding window keeping track of current total
            curr = 0
            #k dimnesion
            for j in range(k + 1):
                if j >= i:
                    curr -= dp[j - i]
                curr =(curr + dp[j]) % MOD
                new_dp[j] = curr
            dp = new_dp
        return dp[k]
