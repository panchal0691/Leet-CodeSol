class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        h = [(0,-1)]
        best = -float("inf")

        for index,num in enumerate(nums):
            total,pindex = h[0]
            while index -pindex >k and len(h) >0:
                heapq.heappop(h)
                total, pindex = h[0]

            current = -total + num
            heapq.heappush(h, ( -current, index))
            heapq.heappush(h, (0,index))
            best = max(current, best)

        return best
        
