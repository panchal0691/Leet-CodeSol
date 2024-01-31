class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []
        for idx, temp in enumerate(temps):
            while stack and temp > stack[-1][1]:
                loc, _ = stack.pop()
                res[loc] = idx - loc
            stack.append((idx, temp))
        return res
