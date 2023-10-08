class Solution:
    def maxDotProduct(self, m: List[int], n: List[int]) -> int:
        if len(m) < len(n):
            m, n = n, m
        if max(n) < 0 and min(m) > 0:
            return max(n) * min(m)
        if max(m) < 0 and min(n) > 0:
            return max(m) * min(n)
        
        M, N = len(m), len(n)
        # visited ={}
        # def dp(i1, i2):
        #     if i1 == M or i2 == N:
        #         return 0
        #     if (i1, i2) in visited:
        #         return visited[(i1, i2)]
        #     visited[(i1, i2)] = max(
        #         m[i1] * n[i2] + dp(i1 + 1, i2 + 1),
        #         dp(i1 + 1, i2),
        #         dp(i1, i2 + 1)
        #     )
        #     return visited[(i1, i2)]
        # return dp(0,0)

        dp = [0 for _ in range(N + 1)]

        for row in range(M - 1, -1, -1 ):
            new_row = [0 for _ in range(N + 1)]
            for col in range(N - 1, -1 , -1):
                new_row[col] = max(
                    m[row] * n[col] + dp[col + 1],
                    new_row[col + 1],
                    dp[col]
                )
            dp = new_row
        return dp[0]
