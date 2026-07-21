from collections import Counter
def solution(clothes):
    c = Counter(kind for name, kind in clothes)
    print(c)
    answer = 1
    
    for i in c.values():
        answer *= i + 1
    
    return answer - 1