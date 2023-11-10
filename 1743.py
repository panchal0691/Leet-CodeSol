class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        N = len(adjacentPairs) + 1
        adj_list = collections.defaultdict(set)
        for u,v in adjacentPairs:
            adj_list[u].add(v)
            adj_list[v].add(u)

        first = next(k for k, v in adj_list.items() if len(v) ==1)
        ans =[first]
        current = first
        for _ in range(N -1):
            assert(len(adj_list[current]) ==1)
            nxt = list(adj_list[current])[0]
            adj_list[nxt].remove(current)
            ans.append(nxt)
            current = nxt
        return ans
        
