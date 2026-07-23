import heapq

def solution(n, works):
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
    time = 0
    while time < n:
        w = -heapq.heappop(heap)
        if w == 0:
            break
        w -= 1
        heapq.heappush(heap, -w)
        time += 1
    
    answer = 0
    for w in heap:
        answer += (-w) ** 2
    return answer