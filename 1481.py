from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        counter = Counter(arr)
        freq = list(counter.values())
        
        # Construct min heap
        heapq.heapify(freq)
        
        elements_removed = 0
        while freq:
            # Remove the least frequent element
            elements_removed += heapq.heappop(freq)
            
            # If the number of elements removed exceeds k, return
            # the remaining number of unique elements
            if elements_removed > k:
                return len(freq) + 1
            
        # We have removed all elements, so no unique integers remain
        # Return 0 in this case
        return 0
