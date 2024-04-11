class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = []  # it will act like a stack
        n = len(num)
        
        for i in range(n):
            while result and result[-1] > num[i] and k > 0:
                result.pop()
                k -= 1
            
            if result or num[i] != '0':
                result.append(num[i])  # to avoid the case when we have preceding zeros
        
        while result and k > 0:
            result.pop()
            k -= 1
        
        if not result:
            return "0"
        
        return ''.join(result)
        
