class Solution:
    def __init__(self):
        self.t = [-1] * 101
    
    def solve(self, i, s, n):
        if self.t[i] != -1:
            return self.t[i]
        
        if i == n:
            self.t[i] = 1  # one valid split done
            return self.t[i]
        
        if s[i] == '0':
            self.t[i] = 0  # not possible to split
            return self.t[i]
        
        result = self.solve(i + 1, s, n)
        
        if i + 1 < n:
            if s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                result += self.solve(i + 2, s, n)
        
        self.t[i] = result
        return self.t[i]

    def numDecodings(self, s):
        n = len(s)
        self.t = [-1] * 101  # Resetting t array
        return self.solve(0, s, n)
