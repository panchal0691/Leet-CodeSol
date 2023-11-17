class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        highest = 0
        for i in range(N):
            highest = max(highest, nums[i] + nums[N -i -1])
        return highest
        
