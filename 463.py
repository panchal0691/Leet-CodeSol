class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.peri = 0
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0:
            self.peri += 1
            return
        
        if grid[i][j] == -1:
            return
        
        grid[i][j] = -1  # mark visited
        
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
    
    def islandPerimeter(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])
        self.peri = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    return self.peri
        
        return -1
