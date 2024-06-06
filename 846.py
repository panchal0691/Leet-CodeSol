from collections import defaultdict
import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize):
        n = len(hand)

        # Check if the total number of cards is divisible by the group size
        if n % groupSize != 0:
            return False

        # Create a dictionary to count the frequency of each card
        count = defaultdict(int)
        for card in hand:
            count[card] += 1

        # Use a min-heap to process the cards in sorted order
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            curr = min_heap[0]

            for i in range(groupSize):
                if count[curr + i] == 0:
                    return False

                count[curr + i] -= 1
                if count[curr + i] == 0:
                    if curr + i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True
