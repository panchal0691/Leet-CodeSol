class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.nodes = n
        self.graph = defaultdict(list)
        for start, end, dist in edges:
            self.graph[start].append([end, dist])
        

    def addEdge(self, edge: List[int]) -> None:
        start, end, dist = edge
        self.graph[start].append([end, dist])
        print(self.graph)
        

    def shortestPath(self, node1: int, node2: int) -> int:
        if min(node1, node2) < 0 or max(node1, node2) >= self.nodes:
            return -1
        heap = [[0, node1]]
        visited = set()
        while heap:
            path, start = heappop(heap)
            if start in visited:
                continue
            visited.add(start)
            if start == node2:
                return path
            for end, dist in self.graph[start]:
                if end not in visited:
                    heappush(heap, [dist + path, end])
        return -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
