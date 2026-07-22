from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    total = sum1 + sum2
    
    if total % 2 == 1:
        return -1
    
    limit = 3 * (len(q1) + len(q2))
    ops = 0
    
    while ops <= limit:
        if sum1 == sum2:
            return ops
        
        if sum1 > sum2:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            sum1 += x
            sum2 -= x
        ops += 1
    return -1