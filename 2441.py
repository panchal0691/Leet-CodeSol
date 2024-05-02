class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        result = -1
        
        for i in nums:
            for j in nums:
               
                if i == -j:
                    
                    result = max(result, abs(i))

        return result
        
