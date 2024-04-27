class Solution:
    def countSteps(self, ringIndex, i, n):
        dist = abs(i - ringIndex)
        wrapAround = n - dist
        return min(dist, wrapAround)
    
    def findRotateSteps(self, ring, key):
        n = len(ring)
        m = len(key)
        
        t = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        # t[ringIndex][keyIndex] = minimum number of steps to get key[keyIndex] when the ring[ringIndex] is aligned with the "12:00" position.

        # Base case when all key characters are done (we reached index n)
        for ringIndex in range(n):
            t[ringIndex][m] = 0
        
        for keyIndex in range(m - 1, -1, -1):
            for ringIndex in range(n):
                result = float('inf')
                for i in range(len(ring)):
                    if ring[i] == key[keyIndex]:
                        totalSteps = self.countSteps(ringIndex, i, len(ring)) + 1 + \
                                     t[i][keyIndex + 1]
                        result = min(result, totalSteps)
                t[ringIndex][keyIndex] = result
        
        return t[0][0]
