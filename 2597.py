class Solution:
    def __init__(self):
        self.result = 0
        self.K = 0

    def dfs(self, nums, idx, mp):
        if idx == len(nums):
            self.result += 1
            return

        # not_take
        self.dfs(nums, idx + 1, mp)

        # checking if we can take it or not
        if (nums[idx] - self.K not in mp or mp[nums[idx] - self.K] == 0) and \
           (nums[idx] + self.K not in mp or mp[nums[idx] + self.K] == 0):
            mp[nums[idx]] = mp.get(nums[idx], 0) + 1
            self.dfs(nums, idx + 1, mp)
            mp[nums[idx]] -= 1
            if mp[nums[idx]] == 0:
                del mp[nums[idx]]

    def beautifulSubsets(self, nums, k):
        self.result = 0
        self.K = k

        mp = {}

        self.dfs(nums, 0, mp)

        return self.result - 1  # -1 because we don't want to count empty subset in result
