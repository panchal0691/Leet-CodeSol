class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = float('inf')
        graph = defaultdict(list)
        shortest = defaultdict(int)
        for start, end, dist in flights:
            graph[start].append((dist, end))
            shortest[start] = float('inf')
            shortest[end] = float('inf')
        queue = deque()
        queue.append((0,0,src))
        while queue:
            dist, stops, city = queue.popleft()
            shortest[city] = min(shortest[city], dist)
            if city == dst:
                res = min(res, dist)
                continue
            if city not in graph or stops > k or shortest[city] != dist:
                continue
            for (trip, loc) in graph[city]:  
                queue.append((dist + trip, stops + 1, loc))
        return res if res != float('inf') else -1
        
