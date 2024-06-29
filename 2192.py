from collections import defaultdict

class Solution:
    def DFS(self, ancestor, adj, currNode, result):
        for ngbr in adj[currNode]:
            if not result[ngbr] or result[ngbr][-1] != ancestor:  # to avoid duplicate entry
                result[ngbr].append(ancestor)
                self.DFS(ancestor, adj, ngbr, result)
    
    def getAncestors(self, n, edges):
        result = [[] for _ in range(n)]
        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)  # u --> v
        
        for i in range(n):
            ancestor = i
            self.DFS(ancestor, adj, i, result)
        
        return result

# Example usage:
# solution = Solution()
# print(solution.getAncestors(4, [[0, 1], [1, 2], [2, 3], [3, 0]]))
