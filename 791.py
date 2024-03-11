class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0] * 26
        
        for x in s:
            count[ord(x) - ord('a')] += 1
        
        result = ""
        for ch in order:
            while count[ord(ch) - ord('a')] > 0:
                result += ch
                count[ord(ch) - ord('a')] -= 1
        
        
        for ch in s:
            if count[ord(ch) - ord('a')] > 0:
                result += ch
        
        return result
        
