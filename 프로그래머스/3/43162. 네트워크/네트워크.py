from collections import deque


def bfs(i, n, computers, visited):
    q = deque()
    q.append(i)
    visited[i] = 1
    
    while q:
        cur = q.popleft()
        
        for nxt in range(n):
            if computers[cur][nxt] == 1 and not visited[nxt]:
                visited[nxt] = 1
                q.append(nxt)
        
def solution(n, computers):
    visited = [0] * n
    group = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i, n, computers, visited)
            group += 1
    
    return group