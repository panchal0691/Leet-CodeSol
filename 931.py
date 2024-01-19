class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)

        cache = {}
        def dp(row, col):
            if col < 0 or col == N:
                return float('inf')
            if row == N:
                return 0
            if (row, col) in cache:
                return cache[(row, col)]
            
            cache[(row, col)] = matrix[row][col] + min(dp(row + 1, col), dp(row + 1, col -1), dp(row + 1, col + 1))
            return cache[(row, col)]
        return min(dp(0, i) for i in range(N))
