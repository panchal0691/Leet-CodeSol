from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        sorted_chars = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        
        result = ""
        for char, freq in sorted_chars:
            result += char * freq
        
        return result
