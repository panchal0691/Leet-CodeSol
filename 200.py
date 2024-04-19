class Solution:
    def __init__(self):
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '$'
        
        for p in self.dir:
            i_ = i + p[0]
            j_ = j + p[1]
            self.dfs(grid, i_, j_)
            
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        
        return count
