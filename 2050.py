class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegrees = [0] * n
        e = collections.defaultdict(list)
        for u,v in relations:
            u -=1
            v -=1

            indegrees[v] +=1
            e[u].append(v)

        q = collections.deque()
        start = [0] * n

        for i in range(n):
            if indegrees[i] ==0:
                q.append(i)
                start[i] = 0
        while len(q) > 0:
            x= q.popleft()

            for u in e[x]:
                indegrees[u] -=1
                start[u] = max(start[u],start[x] + time[x])

                if indegrees[u] ==0:
                    q.append(u)

        return max(start[x] + time [x] for x in range(n))
        
