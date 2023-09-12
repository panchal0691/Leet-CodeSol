class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums_len = len(nums)
        
        last_num = nums_len 
        def func(nums, last_num):
            i = 0
            for i in range(last_num + 1):
                if i not in nums:
                    return i
                
            return i 

        ans = func(nums, last_num)
        return ans
         
        
