class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        N = len(piles)
        piles.sort(reverse = True)
        total =0
        i =0
        j = N -1
        while i <j:
            total += piles[i +1]
            i +=2
            j -=1
        return total
        
