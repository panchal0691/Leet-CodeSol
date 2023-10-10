class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        nums =  list(sorted(set(nums)))
        M = len(nums)

        left = 0
        right =0
        best = 0

        while left < M:
            while right < M and nums[right] - nums[left] <= N -1:
                right +=1

            best = max(best, right - left)
            left +=1
        return N - best
        
