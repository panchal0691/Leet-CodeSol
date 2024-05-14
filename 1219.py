class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def DFS(self, grid, i, j):
        if i >= self.m or i < 0 or j >= self.n or j < 0 or grid[i][j] == 0:
            return 0  # Zero gold

        originalGoldValue = grid[i][j]
        grid[i][j] = 0

        maxGold = 0

        # Up, down, left, right
        for dir in self.directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            maxGold = max(maxGold, self.DFS(grid, new_i, new_j))

        grid[i][j] = originalGoldValue
        return originalGoldValue + maxGold

    def getMaximumGold(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])

        maxGold = 0

        for i in range(self.m):
            for j in range(self.n):

                if grid[i][j] != 0:
                    # It has gold
                    maxGold = max(maxGold, self.DFS(grid, i, j))

        return maxGold

# Example usage:
# sol = Solution()
# grid = [[0,6,0],[5,8,7],[0,9,0]]
# print(sol.getMaximumGold(grid))
