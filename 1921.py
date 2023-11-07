class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        t = []
        for d, s in zip(dist, speed):
            t.append((d/s,d,s))
        t.sort()
        killed = 0
        for x, (_,d,s) in enumerate(t):
            if s*x >= d:
                return killed
            killed +=1
        return killed
