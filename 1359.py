class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        count = 1
        
        for i in range(2, n+1):
            dividers = (i-1) *2

            choices = dividers +1
            count = ((choices* (choices + 1)) //2)* count 
            count %= mod 

        return count % mod

        
