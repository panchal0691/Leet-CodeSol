class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)

        if N1 +N2 != N3:
	        return False

        has_cache = [[False] * (N2 +1) for _ in range(N1 +1)]
        cache = [[None] * (N2 +1) for _ in range(N1+1)]


        def isPossible(i1,i2,i3):
            if i3 == N3:
                return True

            if has_cache[i1][i2]:
                return cache[i1][i2]

            has_cache[i1][i2] = True
            if i1 < N1 and s1[i1] == s3[i3] and isPossible(i1 +1,i2,i3+1):
                cache[i1][i2] = True
                return True

            if i2 < N2 and s2[i2] == s3[i3] and isPossible(i1,i2+1,i3+1):

                cache[i1][i2] = True
                return True


            cache[i1][i2] = False
            return False 

        return isPossible(0,0,0)
