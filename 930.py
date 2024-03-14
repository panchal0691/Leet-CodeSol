from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        
        count = 0
        currSum = 0
        mp[0] = 1
        for num in nums:
            currSum += num

            if currSum - goal in mp:
                count += mp[currSum - goal]

            mp[currSum] += 1

        return count
