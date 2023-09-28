class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_num =0
        for i in range(len(nums)):
            # count = 0
            if (nums[i]%2 == 0):
                nums[i] , nums[even_num] = nums[even_num] , nums[i]

                even_num +=1

        return nums

        
