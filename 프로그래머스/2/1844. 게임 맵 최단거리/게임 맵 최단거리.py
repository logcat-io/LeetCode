from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0,0,1))
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while q:
        cx, cy, d = q.popleft()
        
        if cx == n-1 and cy == m-1:
            return d
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if not maps[nx][ny]: continue
            if visited[nx][ny]: continue
            
            visited[nx][ny] = True
            q.append((nx, ny, d+1))
            
    return -1