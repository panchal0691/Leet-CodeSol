class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        if n == 0:
            return ans
        
        nums.sort()
        max_val = 1
        dp = [1] * (n + 1)
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    if max_val < dp[i]:
                        max_val = dp[i]
        
        # Now push the answer LIS
        prev = -1
        for i in range(n - 1, -1, -1):
            if dp[i] == max_val and (prev % nums[i] == 0 or prev == -1):
                ans.append(nums[i])
                max_val -= 1
                prev = nums[i]
        
        return ans
        
