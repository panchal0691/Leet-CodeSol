class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left, right = 0, n - 1
        result = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1

        return result
        
