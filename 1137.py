class Solution:
    def __init__(self):
        self.t = [-1] * 38

    def find(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if self.t[n] != -1:
            return self.t[n]

        a = self.find(n - 1)
        b = self.find(n - 2)
        c = self.find(n - 3)

        self.t[n] = a + b + c
        return self.t[n]

    def tribonacci(self, n):
        self.t = [-1] * 38
        return self.find(n)

# Example usage:
solution = Solution()
n = 5
print(solution.tribonacci(n))  # Output will be the nth tribonacci number
