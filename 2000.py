class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0
        j = word.find(ch)
        
        while i < j:
            word = list(word)
            word[i], word[j] = word[j], word[i]
            word = ''.join(word)
            i += 1
            j -= 1
        
        return word
        
