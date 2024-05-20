from typing import List

class Solution:
    def solve(self, nums: List[int], i: int, currSubset: List[int], subsets: List[List[int]]) -> None:
        if i == len(nums):
            subsets.append(currSubset[:])
            return
        
        currSubset.append(nums[i])
        self.solve(nums, i + 1, currSubset, subsets)
        currSubset.pop()
        self.solve(nums, i + 1, currSubset, subsets)
    
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        currSubset = []
        self.solve(nums, 0, currSubset, subsets)
        
        result = 0
        for currSubset in subsets:
            xor_value = 0
            for num in currSubset:
                xor_value ^= num
            result += xor_value
        return result
