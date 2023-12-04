class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for x in range(9, -1,-1):
            if str(x)* 3 in num:
                return str(x)*3
        return ""

        
