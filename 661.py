class Solution:
    def __init__(self):
        self.directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 0], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]

    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])

        result = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total_sum = 0
                count = 0

                for direction in self.directions:
                    i_ = i + direction[0]
                    j_ = j + direction[1]

                    if 0 <= i_ < m and 0 <= j_ < n:
                        total_sum += img[i_][j_]
                        count += 1

                result[i][j] = total_sum // count

        return result
