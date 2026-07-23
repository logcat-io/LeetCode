import heapq

def solution(scoville, K):
    if K == 0:
        return 0
    
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    ans = 0
    
    while len(heap) > 1 and heap[0] < K:
        value = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
        heapq.heappush(heap, value)
        ans  += 1
    
    if len(heap) == 1 and heap[0] < K:
        return -1
    
    return ans