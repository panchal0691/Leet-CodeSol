class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cur =[float(poured)]
        for r in range(1, query_row +1):
            nxt = [0.0] * (r +1)

            for c in range(r):
                over = max((cur[c] - 1.0) /2.0, 0.0)
                nxt[c] += over
                nxt[c+1] += over
            cur = nxt
        return min(cur[query_glass], 1.0)
        
