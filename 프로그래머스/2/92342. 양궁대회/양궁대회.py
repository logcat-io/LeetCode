import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, info):
    best = None
    best_diff = 0
    
    def diff_of(ryan):
        ryan_score, apeach_score = 0, 0
        for i in range(11):
            if info[i] == 0 and ryan[i] == 0:
                continue
            if info[i] < ryan[i]:
                ryan_score += 10 -i 
            else:
                apeach_score += 10 - i
        
        return ryan_score - apeach_score
    
    def lower_first(cand, ryan):
        for i in range(10, -1, -1):
            if cand[i] != ryan[i]:
                return cand[i] > ryan[i]
        return False
    
    def bt(idx, left, ryan):
        nonlocal best, best_diff
        
        if idx == 10:
            cand = ryan[:]
            cand[10] = left
            d = diff_of(cand)
            
            if d <= 0:
                return
            if best is None or d > best_diff:
                best, best_diff = cand, d
            elif best_diff == d and lower_first(cand, best):
                best, best_diff = cand, d
            
            return
        
        need = info[idx] + 1
        if need <= left:
            ryan[idx] = need
            bt(idx + 1, left - need, ryan)
            ryan[idx] = 0

        bt(idx+1, left, ryan)
        
        return best
    
    result = bt(0, n, [0]*11)
    return [-1] if result is None else result