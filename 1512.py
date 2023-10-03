
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        my = {}
        gp =0
        for num in nums:
            if num in my:
                gp = gp + my[num]
                my[num] = my[num] +1
            else:
                my[num] = 1
        return gp
        
