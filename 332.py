class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ins = collections.defaultdict(int)
        outs = collections.defaultdict(int)
        edges= collections.defaultdict(lambda : collections.defaultdict(int))
        names = set()

        for u, v in tickets:
            edges [u][v] +=1
            names.add(u)
            names.add(v)

        names = sorted(list(names))
        ans = []

        def construct(node):
            nonlocal ans

            for name in names:
                if name in edges[node] and edges[node][name] > 0:
                    edges[node][name] -=1
                    construct(name)

            ans.append(node)


        construct("JFK")
        ans.reverse()
        return ans
        
