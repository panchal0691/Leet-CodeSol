class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 +7
        has_cache = [[False] * (steps +1) for _ in range(steps +1)]
        cache = [[None] * (steps +1) for _ in range(steps +1)]

        def count(stepsLeft, index):
            if stepsLeft == 0:
                if index ==0:
                    return 1
                return 0

            if stepsLeft < index:
                return 0 
            if has_cache[stepsLeft][index]:
                return cache[stepsLeft][index]

            total = 0
            if index -1 >=0:
                total += count(stepsLeft -1, index -1)
            if index + 1<arrLen:
                total += count(stepsLeft -1,index +1)

            total += count(stepsLeft -1,index)

            has_cache[stepsLeft][index] =True
            cache[stepsLeft][index] = total % MOD
            return total %MOD
        return count(steps, 0) % MOD
        
        
