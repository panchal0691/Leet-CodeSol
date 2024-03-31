class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lastMin = -1
        lastMax = -1
        l = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] < minK or nums[r] > maxK:
                l = r + 1
                continue
            if nums[r] == minK:
                lastMin = r
            if nums[r] == maxK:
                lastMax = r

            if lastMin >= l and lastMax >= l:
                res += min(lastMin, lastMax) - l + 1

        return res
