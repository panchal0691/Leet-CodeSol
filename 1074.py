from typing import List, Dict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # First take the cumulative sum row-wise
        for row in range(rows):
            for col in range(1, cols):
                matrix[row][col] += matrix[row][col - 1]

        # Now, find the "No. of subarrays with sum k" in the downward direction
        result = 0
        for startCol in range(cols):
            for currCol in range(startCol, cols):
                # We need to find all submatrices sum

                # Now comes the concept of "No. of subarrays with sum k"
                _map: Dict[int, int] = {0: 1}
                _sum = 0

                # Go downwards row-wise
                for row in range(rows):
                    _sum += matrix[row][currCol] - (matrix[row][startCol - 1] if startCol > 0 else 0)

                    if _sum - target in _map:
                        result += _map[_sum - target]

                    _map[_sum] = _map.get(_sum, 0) + 1

        return result
