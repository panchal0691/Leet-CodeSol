class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])
        left = 0
        right = (10 **6) + 10 

        directions = [
            (1,0), (0,1), (-1,0), (0,-1),
        ]

        def good(target):
            done = [[False] * C for _ in range(R)]



            q = collections.deque()
            q.append((0,0))
            done[0][0] = True

            while len(q ) > 0:
                x,y = q.popleft()

                if x == R-1 and y == C-1:
                    return True

                for dx, dy in directions:
                    nx , ny = x +dx, y + dy

                    if 0 <= nx <R and 0 <= ny < C and not done[nx][ny] and abs(heights[x][y] - heights[nx][ny]) <= target:
                        done[nx][ny] =True
                        q.append((nx, ny))

            return False


        while left < right:
            mid = (left + right) //2

            if good(mid):
                right = mid

            else:
                left = mid +1
        return left
    
