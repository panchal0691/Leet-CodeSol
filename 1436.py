class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        od = collections.Counter()
        for u,v in paths:
            od[u] +=1
            od[v] +=0

        for key in od.keys():
            if od[key] == 0:
                return key
        assert(False)
        
