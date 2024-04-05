class Solution:
    def makeGood(self, s: str) -> str:
        result = ""
        
        for ch in s:
            if result and (ch.lower() == result[-1].lower() and ch.islower() != result[-1].islower()):
                result = result[:-1]
            else:
                result += ch
        
        return result
        
