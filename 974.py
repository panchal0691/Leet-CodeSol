from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums, k):
        n = len(nums)
        
        mp = defaultdict(int)
        sum = 0
        
        mp[0] = 1
        
        result = 0
        
        for i in range(n):
            sum += nums[i]
            
            rem = sum % k
            
            if rem < 0:
                rem += k
            
            if rem in mp:
                result += mp[rem]
            
            mp[rem] += 1
        
        return result
