class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        offset =0
        for x in range(1, n +1):
            t = x % 7
            if t %7 ==0:
                t += 7
            total += offset +t
            if x % 7 ==0:
                offset +=1
        return total
        
