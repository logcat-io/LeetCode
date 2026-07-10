class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        s = [[0] * (m+1) for _ in range(n+1)]
        answer = [[0] * m for _ in range(n)]

        for i in range(n):
            r = 0
            for j in range(m):
                r += mat[i][j]
                s[i+1][j+1] = s[i][j+1] + r
        
        for i in range(n):
            for j in range(m):
                r1 = max(0, i-k)
                c1 = max(0, j-k)
                r2 = min(n-1, i+k)
                c2 = min(m-1, j+k)
            
                total = s[r2+1][c2+1]
                total -= s[r2+1][c1]
                total -= s[r1][c2+1]
                total += s[r1][c1]
                
                answer[i][j] = total
        
        return answer