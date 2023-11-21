class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse_number(num):
            res = 0
            while num:
                res = res * 10 + num % 10
                num //= 10
            return res
        MOD = 10**9 + 7
        counts = defaultdict(int)
        pairs = 0
        for num in nums:
            diff = num - reverse_number(num)
            pairs += counts[diff]
            counts[diff] += 1
        return pairs % MOD
