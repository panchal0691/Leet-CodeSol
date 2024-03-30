from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        
        i_chota = 0
        j = 0
        i_bada = 0
        
        result = 0
  
        while j < n:
            mp[nums[j]] += 1
            
            while len(mp) > k:
                mp[nums[i_chota]] -= 1
                if mp[nums[i_chota]] == 0:
                    del mp[nums[i_chota]]
                i_chota += 1
                i_bada = i_chota
            
            while mp[nums[i_chota]] > 1:
                mp[nums[i_chota]] -= 1
                i_chota += 1
            
            if len(mp) == k:
                result += i_chota - i_bada + 1
            j += 1
        
        return result
