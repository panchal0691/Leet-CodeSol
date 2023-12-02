class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        chars_count = collections.Counter(chars)
        def good(word, chars):
            word_count = collections.Counter(word)

            for c in word_count.keys():
                if word_count[c] > chars_count[c]:
                    return False
            return True

        for word in words:
            if good(word, chars):
                ans += len(word)

        return ans
        
