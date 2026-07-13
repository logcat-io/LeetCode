from collections import Counter
def solution(nums):
    h = len(nums) // 2
    nc = Counter(nums)
    answer = min(h, len(nc.keys()))
    return answer