class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N =  len(graph)
        INF = 10**20

        d = [[INF] *N for _ in range(N)]

        for i in range(N):
            d[i][i] = 0
            for v in graph[i]:
                d[i][v] = d[v][i] =1

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        has_cache = [[False] * (2** N ) for _ in range(N)]
        cache = [[None] * (2**N) for _ in range(N)]

        def to_binary(seen):
            current = 0

            for v in seen:
                current *= 2
                if v:
                    current +=1
            return current


        def calc(current, seen):
            if all(seen):
                return 0

            bseen = to_binary(seen)
            if has_cache[current][bseen]:
                return cache[current][bseen]

            best = INF
            for v in range(N):
                if not seen[v]:
                    seen[v] =True
                    best = min(best, calc(v, seen) + d[current][v])
                    seen[v] = False
            has_cache[current][bseen] = True
            cache[current][bseen] = best
            return best

        best = INF
        for start in range(N):
            seen = [False] * N

            seen[start] = True

            best = min(best, calc(start, seen))

        return best

                


        
