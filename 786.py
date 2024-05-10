import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        pq = []
        
        for i in range(n):
            heapq.heappush(pq, [1.0 * arr[i] / arr[-1], float(i), float(n - 1)])
        
        smallest = 1
        
        while smallest < k:
            vec = heapq.heappop(pq)
            i = int(vec[1])
            j = int(vec[2]) - 1
            
            heapq.heappush(pq, [1.0 * arr[i] / arr[j], float(i), float(j)])
            smallest += 1
        
        vec = heapq.heappop(pq)
        i = int(vec[1])
        j = int(vec[2])
        
        return [arr[i], arr[j]]
