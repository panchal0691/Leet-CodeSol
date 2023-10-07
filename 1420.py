class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        has_cache = [[[False] * (k +1) for _ in range(m+1)] for _ in range(n +1)]
        cache = [[[None] * (k +1) for _ in range(m+1)] for _ in range(n+1)]
        def count(N, mx,K):
            if N ==0:
                if K ==0:
                    return 1
                return 0
            if has_cache[N][mx][K]:
                return cache[N][mx][K]

            c=0
            for x in range(1,mx+1):
                c += count(N -1,mx,K)
                c %= MOD

            if K> 0:
                for x in range(mx +1, m+1):
                    c += count(N -1,x,K-1)
                    c %= MOD

            has_cache[N][mx][K] = True
            cache[N][mx][K] = c% MOD
            return c%MOD
        return count(n,0,k)%MOD
        
