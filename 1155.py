class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        cache = {}
        def dp(dice, total):
            if dice == n:
                return total == 0
            if total < 0:
                return 0
            if (dice, total) in cache:
                return cache[(dice, total)]
            
            res = 0
            for i in range(1, k + 1):
                res = (res + dp(dice + 1, total - i)) % MOD
            cache[(dice, total)] = res
            return res
        return dp(0, target)
