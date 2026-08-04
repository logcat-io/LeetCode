def solution(board, skill):
    n = len(board)
    m = len(board[0])
    diff = [[0] * (m+1) for _ in range(n+1)]
    
    for t, r1, c1, r2, c2, de in skill:
        if t == 1:
            de *= -1
        
        diff[r2+1][c2+1] += de
        diff[r2+1][c1] -= de
        diff[r1][c2+1] -= de
        diff[r1][c1] += de
    
    for i in range(n):
        for j in range(1, m):
            diff[i][j] += diff[i][j-1]
    for i in range(n):
        for j in range(1, m):
            diff[j][i] += diff[j-1][i]
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if (board[i][j] + diff[i][j]) > 0:
                ans += 1
    return ans