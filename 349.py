from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1 = set(nums1)
        st2 = set()
        
        for num in nums2:
            if num in st1:
                st2.add(num)
        
        return list(st2)
