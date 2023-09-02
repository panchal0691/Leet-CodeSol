class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        has_cache = [False]*N
        cache = [None]*N

        def getMin(index):
            if index == N:
                return 0

            if has_cache[index]:
                return cache[index]

            best = getMin(index+1)+1
            used = set()

            for word in dictionary:
                if len(word) not in used and s[index:].startswith(word):
                    used.add(len(word))
                    best = min(best, getMin(index + len(word)))

            has_cache[index]= True

            cache[index]= best 
            return best

        return getMin(0)
        
