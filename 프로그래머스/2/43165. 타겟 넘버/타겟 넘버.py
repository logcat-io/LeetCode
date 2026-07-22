from collections import deque

def bfs(numbers, target):
    count = 0
    q = deque()
    q.append((numbers[0], 0))
    q.append((numbers[0] * -1, 0))
    
    while q:
        n = len(q)
        
        for i in range(n):
            cur, idx = q.popleft()
            
            if cur == target and idx == len(numbers) - 1:
                count += 1
            
            if idx + 1 >= len(numbers): continue
            
            nxt = numbers[idx + 1]
            q.append((cur + nxt, idx + 1))
            q.append((cur - nxt, idx + 1))
    
    return count

def solution(numbers, target):
    
    return bfs(numbers, target)