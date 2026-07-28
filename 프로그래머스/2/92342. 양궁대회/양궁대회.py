import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, info):
    best = []
    best_diff = -1
    
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
    
    def bt(pos, start, n, ryan):
        nonlocal best, best_diff
        
        if pos == n:
            diff = diff_of(ryan[:])
            if diff <= 0:
                return
            if diff > best_diff:
                best_diff = diff
                best = [ryan[:]]
            elif best_diff == diff:
                best.append(ryan[:])
            return
        
        for i in range(start, 11):
            ryan[i] += 1
            bt(pos + 1, i, n, ryan)
            ryan[i] -= 1
        
        return best

    result = bt(0,0, n, [0]*11)
    
    if best_diff < 0:
        return [-1]
    
    result.sort(key=lambda arr: arr[::-1], reverse=True)
    return result[0]