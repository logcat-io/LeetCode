import heapq

def solution(scoville, K):
    if K == 0:
        return 0
    
    heapq.heapify(scoville)
    ans = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        value = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, value)
        ans  += 1
    
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    
    return ans