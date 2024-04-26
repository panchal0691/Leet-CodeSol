class Solution:
    def __init__(self):
        self.n = 0
        self.t = [[-1] * 201 for _ in range(201)]

    def solve(self, row, col, grid):
        if row == self.n - 1:
            return grid[row][col]

        if self.t[row][col] != -1:
            return self.t[row][col]

        ans = float('inf')
        for nextCol in range(self.n):
            if nextCol != col:
                ans = min(ans, self.solve(row + 1, nextCol, grid))

        self.t[row][col] = grid[row][col] + ans
        return self.t[row][col]

    def minFallingPathSum(self, grid):
        self.n = len(grid)

        result = float('inf')
        for col in range(self.n):
            result = min(result, self.solve(0, col, grid))

        return result

# Example usage:
# sol = Solution()
# grid = [[2,1,3],[6,5,4],[7,8,9]]
# print(sol.minFallingPathSum(grid))
