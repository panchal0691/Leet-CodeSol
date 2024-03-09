class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        st = set(nums1)
        
        for num in nums2:
            if num in st:
                return num
        
        return -1
        
