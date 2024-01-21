class HouseRobber:
    def rob(self, nums):
        # If only 1 element, just return it
        if len(nums) < 2:
            return nums[0]

        # Create list to store the maximum loot at each index
        dp = [0] * len(nums)

        # Memoize maximum loots at first 2 indexes
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Use them to fill the complete list
        for i in range(2, len(nums)):
            # Core logic
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

# Example usage
nums = [2, 7, 9, 3, 1]
robber = HouseRobber()
result = robber.rob(nums)
print(result)
