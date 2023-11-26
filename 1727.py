class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        for x in range(1,R):
            for y in range(C):
                if matrix[x -1][y] > 0 and matrix[x][y]>0:
                    matrix[x][y] += matrix[x -1][y]



        best = 0
        for row in matrix:
            row.sort(reverse = True)
            for i in range(C):
                best = max(best, row[i]*(i + 1))
        return best
        
