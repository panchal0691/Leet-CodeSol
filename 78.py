class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        tot = [[]]
        for i in nums:
            tot += [[i]+j for j in tot]
        return tot
        
