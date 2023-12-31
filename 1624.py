class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mx = -1
        for x,a in enumerate(s):
            for y,b in enumerate(s):
                if a == b and x != y:
                    mx = max(mx, abs(x - y)-1)

        return mx
        
