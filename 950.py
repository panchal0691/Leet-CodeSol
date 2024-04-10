class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [0] * n
        
        skip = False
        
        deck.sort()
        
        i = 0  # index for deck
        j = 0  # index for result
        
        while i < n:
            if result[j] == 0:
                if not skip:
                    result[j] = deck[i]
                    i += 1
                
                skip = not skip  # toggle skip
                
            j = (j + 1) % n
        
        return result
        
