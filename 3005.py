from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr = [0] * 101
        
        maxFreq = 0
        
        for num in nums:
            arr[num] += 1
            maxFreq = max(maxFreq, arr[num])
        
        return arr.count(maxFreq) * maxFreq
