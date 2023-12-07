class Solution:
    def largestOddNumber(self, num: str) -> str:
        last = len(num) -1

        while last >=0:
            if int(num[last]) % 2 ==1:
                return num[:last +1]
            last -= 1
        return ""
        
