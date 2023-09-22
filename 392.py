class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index =0
        t_n = len(t)
        for c in s:
            while t_index < t_n and t[t_index] != c:
                t_index +=1
            if t_index == t_n:
                return False
            t_index +=1


        return True
