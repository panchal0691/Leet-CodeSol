from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        mp = defaultdict(int)
        
        i = 0
        j = 0
        result = 0
        
        while j < n:
            mp[nums[j]] += 1
            
            while i < j and mp[nums[j]] > k:
                mp[nums[i]] -= 1
                i += 1
            
            result = max(result, j - i + 1)
            j += 1
        
        return result
        
