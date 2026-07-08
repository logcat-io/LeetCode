class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        m = len(matrix[0])

        r = [0] * n
        c = [0] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    r[i] = -1
                    c[j] = -1

        for i in range(n):
            for j in range(m):
                if r[i] == -1 or c[j] == -1:
                    matrix[i][j] = 0
      
        """
        Do not return anything, modify matrix in-place instead.
        """
        