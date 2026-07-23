class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        if n == 1 and m == 1:
            return [matrix[0][0]]

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        direction = 0
        block = 0
        r, c = 0, 0
        ans = []
        while block < 2:
            nr, nc = r + dx[direction], c + dy[direction]

            if nr < 0 or nr >= n or nc < 0 or nc >= m or matrix[nr][nc] == -999:
                direction = (direction + 1) % 4 
                block += 1
                continue
            
            ans.append(matrix[r][c])
            matrix[r][c] = -999
            r,c = nr, nc
            block = 0
        ans.append(matrix[r][c])
        return ans



        