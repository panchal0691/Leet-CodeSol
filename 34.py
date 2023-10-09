class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index = bisect.bisect_left(nums, target)
        if not (0 <= first_index < len(nums)) or nums[first_index] != target:
            return [-1,-1]

        last_index = bisect.bisect_right(nums, target) -1
        return [first_index, last_index]
        
