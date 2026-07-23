class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        mark = [[1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    mark[i][j] = 0

        for i in range(n):
            for j in range(m):
                if mark[i][j]:
                    continue
                
                for w in range(n):
                    matrix[w][j] = 0

                for w in range(m):
                    matrix[i][w] = 0

        """
        Do not return anything, modify matrix in-place instead.
        """
        