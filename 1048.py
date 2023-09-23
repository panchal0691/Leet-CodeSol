class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        N = len(words)

        words.sort(key = lambda w: len(w))

        best = {}
        bestbest =0
        for word in words:
            longest = 1

            for i in range(len(word)):
                current = word[:i] + word[i + 1:]

                if current in best:
                    longest = max(longest, best[current] +1)
            best[word] = longest
            bestbest = max(bestbest, longest)

        return bestbest
        
