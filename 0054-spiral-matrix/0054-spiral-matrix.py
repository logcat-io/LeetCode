class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        ans = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        r,c = 0, 0
        d = 0 
        cnt = 0
        while True:    
            nr = r + dx[d]
            nc = c + dy[d]

            if nr < 0 or nr >= n or nc < 0 or nc >= m or matrix[nr][nc] == -999:
                d = (d+1) % 4
                cnt += 1
                if cnt == 2:
                    break
                continue

            ans.append(matrix[r][c])
            matrix[r][c] = -999
            r = nr
            c = nc
            cnt = 0
        ans.append(matrix[r][c])
        return ans



        