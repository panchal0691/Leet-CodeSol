class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        last = ['.', 0]
        res = 0
        for color, time in zip(colors, neededTime): 
            if color == last[0]:
                res += min(time, last[1])
                last[1] = max(time, last[1])
            else:
                last = [color, time]
        return res
