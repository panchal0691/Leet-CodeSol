# Radix Sort
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for k,t in queries:
            arr = []
            for i,x in enumerate(nums):
                arr.append((int(x[-t:]), i))
            arr.sort()
            ans.append(arr[k-1][1])
        return ans
        
