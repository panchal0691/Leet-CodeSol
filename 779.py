class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n ==1: return 0
        parent = self.kthGrammar(n-1,k/2 + k%2)
        isKOdd = k%2 ==1
        if parent ==1: 
            return 1 if isKOdd else 0
        else:
            return 0 if isKOdd else 1
