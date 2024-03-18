class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: x[1])
        
        count = 1
        lastEndPoint = points[0][1]
        
        for i in range(1, n):
            curr_startPoint = points[i][0]
            
            if curr_startPoint > lastEndPoint:
                count += 1
                lastEndPoint = points[i][1]
        
        return count
        
