"""
1 <= 던전의 개수 <= 8

최소 필요 피로도, 소모 피로도

던전의 순서가 중요

바뀌면 답도 변경될 수 있다.

유저가 탐험할 수 있는 최대 던전 수를 반환

1. 순서를 변경해서 돌아도 되는 점을 빼먹음 
2. 가능한 모든 순열을 만든다.


"""

def permute(nums):
    res, path = [], []
    used = [False] * len(nums)
    def bt():
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            used[i] = True
            path.append(nums[i])
            bt()
            path.pop()
            used[i] = False
    bt()
    return res
            

def solution(k, dungeons):
    res, path = [], []
    best = 0
    results = permute(dungeons)
    
    for r in results:
        temp_k = k
        stage = 0
        for n, c in r:
            if temp_k >= n:
                temp_k -= c
                stage += 1
            else:
                break
        
        best = max(best, stage)
    
    return best