class Solution:
    def minOperations(self, s: str) -> int:
        b0 = b1 = 0
        for index, x in enumerate(s):
            if index %2 == int(x):
                b0 +=1
            else:
                b1 +=1
        return min(b0,b1)
        
