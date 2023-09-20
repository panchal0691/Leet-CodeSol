class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        INF = 10 **20
        N = len(nums)
        best = INF
        if sum(nums) < x:
            return -1
        sf = N
        ct = 0
        while ct < x and sf >0:
            sf -=1
            ct +=nums[sf]

        if ct == x:
            best = min(best, N-sf )

        for pf in range(N):
            ct += nums[pf]
            while pf >= sf:
                ct -= nums[sf]
                sf +=1
            while sf < N and ct >x:
                ct -= nums[sf]
                sf +=1
            if ct ==x:
                best = min(best, pf +1 + N - sf)
        if best >= INF:
            return -1

        return best


        
