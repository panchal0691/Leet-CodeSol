class Solution:
    def findLocalMax(self, grid, x, y):
        maxElement = 0
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                maxElement = max(maxElement, grid[i][j])
        return maxElement
    
    def largestLocal(self, grid):
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                maxLocal[i][j] = self.findLocalMax(grid, i, j)
        return maxLocal
