class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        board = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n):
            row = 0
            for j in range(m):
                row += mat[i][j]
                board[i+1][j+1] = board[i][j+1] + row

        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                r1, c1 = max(i - k, 0), max(j-k, 0)
                r2, c2 = min(i + k, n-1), min(j+k, m-1)
                total = board[r2+1][c2+1]
                total -= board[r2+1][c1]
                total -= board[r1][c2+1]
                total += board[r1][c1] 
                ans[i][j] = total
        return ans