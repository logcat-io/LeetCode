def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    best = 0
    
    def bt(fatigue, count):
        nonlocal best
        best = max(best, count)
        for i in range(n):
            need, cost = dungeons[i]
            if visited[i]:
                continue
            
            if fatigue < need:
                continue
            
            visited[i] = True
            bt(fatigue-cost, count + 1)
            visited[i] = False
    bt(k, 0)
    return best