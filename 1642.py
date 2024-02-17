import heapq

class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        pq = []
        
        for i in range(len(heights) - 1):
            if heights[i] >= heights[i + 1]:
                continue
            
            bricks -= heights[i + 1] - heights[i]
            heapq.heappush(pq, -(heights[i + 1] - heights[i]))

            if bricks < 0:
                bricks += -heapq.heappop(pq)
                if ladders > 0:
                    ladders -= 1
                else:
                    return i
        
        return len(heights) - 1
