class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = corridor.count('S')
        if seats < 2 or seats % 2 != 0:
            return 0
        seats = 0
        last_seat = 0
        res = 1
        MOD = 10**9 + 7
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                seats += 1
                if seats % 2 == 0:
                    last_seat = i
                elif seats > 1:
                    res *= (i - last_seat)
        return res % MOD
        
