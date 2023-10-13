class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        N = len(cost)
        has_cache = [False] * (N+1)
        cache = [None] * (N+1)
        def f(index):
            if index <= 1:
                return cost[index]

            if has_cache[index]:
                return cache[index]

            ans =  min(
                f(index -1),
                f(index -2)
            ) + cost[index]

            has_cache[index] = True
            cache[index] = ans

            return ans

        return f(N-1)
        
