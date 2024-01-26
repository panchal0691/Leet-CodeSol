class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def findPaths(self, m, n, maxMove, startRow, startColumn):
        dp = [[[0] * 51 for _ in range(50)] for _ in range(50)]

        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for dir in self.directions:
                        x, y = i + dir[0], j + dir[1]
                        if x < 0 or x >= m or y < 0 or y >= n:
                            dp[i][j][k] = (dp[i][j][k] + 1) % self.MOD
                        else:
                            dp[i][j][k] = (dp[i][j][k] + dp[x][y][k - 1]) % self.MOD

        return dp[startRow][startColumn][maxMove]
