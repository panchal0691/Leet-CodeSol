from typing import List, Dict

class Solution:
    def check(self, mp: Dict[int, List[int]], node: int, dest: int, visited: List[bool]) -> bool:
        if node == dest:
            return True
        
        if visited[node]:
            return False
        
        visited[node] = True
        for neighbor in mp[node]:
            if self.check(mp, neighbor, dest, visited):
                return True
        return False
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        mp = {}
        for u, v in edges:
            mp.setdefault(u, []).append(v)
            mp.setdefault(v, []).append(u)
        
        visited = [False] * n
        return self.check(mp, source, destination, visited)
