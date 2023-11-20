class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def calc(t):
            total =0
            current =0
            for i , g in enumerate(garbage):
                if i -1 >= 0:
                    current += travel[i -1]
                if t in g:
                    current += g.count(t)
                    total = current
            return total
        return calc("P") + calc("M") + calc("G")
        
