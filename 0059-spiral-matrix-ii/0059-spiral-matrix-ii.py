class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0

        board = [[0 for _ in range(n)] for _ in range(n)]
        board[0][0] = v = 1

        count = 0
        r, c  = 0, 0

        while True:
            nr = r + dx[d]
            nc = c + dy[d]

            if nr < 0 or nr >= n or nc < 0 or nc >= n or board[nr][nc] != 0:
                d = (d + 1) % 4
                count += 1

                if count == 2:
                    break
                
                continue
            
            v += 1
            count = 0
            board[nr][nc] = v
            r,c = nr, nc
        
        return board