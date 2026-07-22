from collections import Counter

def solution(want, number, discount):
    memo = {k:v for k, v in zip(want, number)}
    n = len(discount)
    ans = 0
    for i in range(n - 10 + 1):
        if Counter(discount[i: i+ 10]) == memo:
            ans += 1
    
    return ans