class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        root = int(n ** 0.5)
        if root * root != n:
            return False
        return (n & (n -1)) ==0 and (root &  (root -1)) == 0
