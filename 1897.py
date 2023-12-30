class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = defaultdict(int)
        w = len(words)
        for word in words:
            for char in word:
                c[char] +=1
        for val in c.values():
            if val%w:
                return False

        return True
        
