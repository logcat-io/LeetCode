def solution(data, ext, val_ext, sort_by):
    memo = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    answer = []
    for d in data:
        tidx = memo[ext]
        
        if d[tidx] < val_ext:
            answer.append(d)
    
    answer = sorted(answer, key=lambda x: x[memo[sort_by]])
    return answer