from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = Counter(arr)
        freq_set = set()

        for freq in freq_map.values():
            if freq in freq_set:
                return False
            freq_set.add(freq)

        return True
