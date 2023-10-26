class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9+7
        s = set(arr)
        lookup = {}

        def calc(x):
            total = 1

            if x in lookup:
                return lookup[x]

            for left in s :
                if x% left ==0 and x // left in s:
                    right = x // left

                    total += calc(left) * calc(right)
                    total %= MOD
            lookup[x] = total % MOD
            return total%MOD
        ans = 0
        for x in s:
            ans += calc(x)
            ans %= MOD
        return ans%MOD
        
