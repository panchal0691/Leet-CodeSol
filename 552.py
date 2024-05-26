class Solution:
    def __init__(self):
        self.M = int(1e9 + 7)

    def checkRecord(self, n: int) -> int:
        t = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(100001)]

        # Base Case - 0 number of days. So, t[0][A][L] = 1
        for A in range(2):
            for L in range(3):
                t[0][A][L] = 1

        for i in range(1, n + 1):
            for A in range(2):
                for L in range(3):
                    result = t[i - 1][A][0]  # P ---> solve(n-1, absent, 0) % M
                    if L < 2:
                        result += t[i - 1][A][L + 1]  # L ---> solve(n-1, absent, consecutive_late+1) % M
                    if A == 0:
                        result += t[i - 1][A + 1][0]  # A ---> solve(n-1, absent+1, 0) % M

                    t[i][A][L] = result % self.M

        return t[n][0][0]  # ---> return solve(n, 0, 0)

# Example usage:
# sol = Solution()
# result = sol.checkRecord(5)
# print(result)  # Output will be the number of valid attendance records
