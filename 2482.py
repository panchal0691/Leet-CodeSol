class Solution:
    def onesMinusZeros(self, grid):
        m = len(grid)
        n = len(grid[0])
        row1 = [0] * m
        row0 = [0] * m
        col1 = [0] * n
        col0 = [0] * n

        for i in range(m):
            r0 = 0
            r1 = 0
            for j in range(n):
                if grid[i][j] == 0:
                    r0 += 1
                else:
                    r1 += 1
            row1[i] = r1
            row0[i] = r0

        for j in range(n):
            c0 = 0
            c1 = 0
            for i in range(m):
                if grid[i][j] == 0:
                    c0 += 1
                else:
                    c1 += 1
            col1[j] = c1
            col0[j] = c0

        diff = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                diff[i][j] = row1[i] + col1[j] - row0[i] - col0[j]

        return diff

# Example usage:
sol = Solution()
grid_example = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]
result = sol.onesMinusZeros(grid_example)
print(result)
