from collections import defaultdict

def solution(gems):
    unique = len(set(gems))
    count = defaultdict(int)

    left =0 
    ax, ay = 0, len(gems) - 1

    for right in range(len(gems)):
        gem = gems[right]
        count[gem] += 1
        
        while len(count) == unique:
            if right - left < ay - ax:
                ax, ay = left, right
            
            left_gem = gems[left]
            count[left_gem] -= 1
            if count[left_gem] == 0:
                del count[left_gem]
            left += 1

    return [ax+1, ay+1]