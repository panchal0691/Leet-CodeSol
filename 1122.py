from typing import List
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Dictionary to store the frequency of elements in arr1
        frequency = defaultdict(int)
        
        # Populate the frequency dictionary with elements from arr1
        for num in arr1:
            frequency[num] += 1

        i = 0
        # Sort elements from arr1 based on the order in arr2
        for num in arr2:
            while frequency[num] > 0:
                arr1[i] = num
                i += 1
                frequency[num] -= 1

        # Append the remaining elements not in arr2, sorted
        for num in sorted(frequency.keys()):
            while frequency[num] > 0:
                arr1[i] = num
                i += 1
                frequency[num] -= 1

        return arr1
