class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [None]*N
        ans[0] = 0

        for i in range(N):
            ans[0] += nums[i] - nums[0]

        for i in range(1,N):
            delta = abs(nums[i] - nums[i -1])
            ans[i] = ans[i -1] + i*delta - (N -i)*delta
        return ans
        
