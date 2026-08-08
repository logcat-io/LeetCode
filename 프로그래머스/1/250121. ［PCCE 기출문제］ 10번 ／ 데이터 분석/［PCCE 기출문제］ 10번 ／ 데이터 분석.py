def solution(data, ext, val_ext, sort_by):
    memo = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    return sorted(filter(lambda x : x[memo[ext]] < val_ext, data), key=lambda x: x[memo[sort_by]])