def solution(board, skill):
    n = len(board)
    m = len(board[0])
    
    diff = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for t, r1, c1, r2, c2, d in skill:
        if t == 1: d *= -1
        
        diff[r1][c1] += d
        diff[r1][c2+1] -= d
        diff[r2+1][c1] -= d
        diff[r2+1][c2+1] += d
    
    for i in range(n):
        for j in range(1, m):
            diff[i][j] += diff[i][j-1]
    
    for i in range(m):
        for j in range(1, n):
            diff[j][i] += diff[j-1][i]
            
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] > 0:
                answer += 1
    
    return answer