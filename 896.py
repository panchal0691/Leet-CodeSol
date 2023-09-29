class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def ist(arr):
            for x,y in zip(arr, arr[1:]):
                if x > y:
                    return False
            return True

        return ist(nums) or ist(list(reversed(nums)))
                  
