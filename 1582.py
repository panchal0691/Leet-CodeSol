class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])
        rows = [0] * R
        cols = [0]*C

        for i in range(R):
            for j in range(C):
                if mat[i][j] ==1:
                    rows[i] +=1
                    cols[j] += 1

        count = 0
        for i in range(R):
            for j in range(C):
                if mat[i][j] ==1 and rows[i] ==1 and cols[j] ==1:
                    count +=1
        return count
