class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)
        dp = [[float("inf")] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i + 1, d + 1)):
                max_difficulty = 0
                for k in range(i, 0, -1):
                    max_difficulty = max(max_difficulty, jobDifficulty[k - 1])
                    dp[i][j] = min(dp[i][j], dp[k - 1][j - 1] + max_difficulty)
        return -1 if dp[n][d] == float("inf") else dp[n][d]
