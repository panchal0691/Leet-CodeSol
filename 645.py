from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        miss, dup = 0, 0

        counter = Counter(nums)

        for i in range(1, n + 1):
            if i in counter:
                if counter[i] == 2:
                    dup = i
            else:
                miss = i

        return [dup, miss]
