class Solution:
    def minOperations(self, nums: List[int]) -> int:
        f = collections.Counter()
        for x in nums:
            f[x] +=1
        total =0
        for v in f.values():
            if v == 1:
                return -1
            total += (v +2)//3
        return total
        
