class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n):
            num = abs(nums[i])
            if nums[num-1] < 0:
                result.append(num)
            else:
                nums[num-1] *= -1
        
        return result

        
