class Solution:
    def matrixScore(self, grid):
        m = len(grid)
        n = len(grid[0])

        # set first column value in each row
        for i in range(m):
            if grid[i][0] == 0:
                # flip that row
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]  # flipping

        for j in range(1, n):
            countZero = sum(1 for i in range(m) if grid[i][j] == 0)
            countOne = m - countZero
            if countZero > countOne:
                # flipping that column
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        score = 0
        for i in range(m):
            for j in range(n):
                value = grid[i][j] * pow(2, n - j - 1)
                score += value

        return score

# Example usage:
# grid = [[1,1,0],[1,0,1],[0,0,0]]
# solution = Solution()
# result = solution.matrixScore(grid)
