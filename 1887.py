class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        previous = nums[0]
        ans = 0
        
        for i in range(1, n):
            if previous != nums[i]:
                ans += n - i
                previous = nums[i]
        
        return ans

        
