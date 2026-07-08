class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        m = len(matrix[0])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        sets = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 0 or (i,j) in sets:
                    continue
                
                r, c = i, j
                sets.add((r, c))
                while r - 1 >= 0:
                    if matrix[r-1][c] != 0:
                        sets.add((r-1,c))

                    matrix[r-1][c] =0
                    r -= 1
                
                r, c = i, j
                while r + 1 < n:
                    if matrix[r+1][c] != 0:
                        sets.add((r+1,c))

                    matrix[r+1][c] =0
                    r += 1
                r, c = i, j
                while c + 1 < m:
                    if matrix[r][c+1] != 0:
                        sets.add((r,c+1))

                    matrix[r][c+1] =0
                    c += 1
                r, c = i, j
                while c - 1 >= 0:
                    if matrix[r][c-1] != 0:
                        sets.add((r,c-1))

                    matrix[r][c-1] =0
                    c -= 1
        """
        Do not return anything, modify matrix in-place instead.
        """
        