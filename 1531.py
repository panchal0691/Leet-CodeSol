class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}
        def counts(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            return 1 + len(str(num))
            
        def dp(idx, last, count, deletions):
            #cached
            if (idx, last, count, deletions) in cache:
                return cache[(idx, last, count, deletions)]
            
            #out of bounds
            if idx == len(s):
                #if we havent used all deletions this cant be the best option
                if deletions > 0:
                    cache[(idx, last, count, deletions)] =  float('inf')
                #cache the result
                else:
                    cache[(idx, last, count, deletions)] =  counts(count)
                return cache[(idx, last, count, deletions)]
            
            res = float('inf')
            #delete
            if deletions != 0:
                res = min(res, dp(idx + 1, last, count, deletions - 1))
            #keep
            #same letter
            if s[idx] == last:
                res = min(res, dp(idx + 1, last, count + 1, deletions))

            #new letter
            else:
                res = min(res, counts(count) + dp(idx + 1, s[idx], 1, deletions))
            cache[(idx, last, count, deletions)] = res
            return res
        
        return dp(0, '.', 0, k)
