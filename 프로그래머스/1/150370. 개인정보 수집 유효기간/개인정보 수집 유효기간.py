def to_days(day, terms_days):
    MONTH_DAYS = 28
    year, month, day = day.split(".")
    return (int(year) * 12 + int(month) + terms_days) * MONTH_DAYS + int(day)

def solution(today, terms, privacies):
    terms_dict = {}
    todays = to_days(today, 0)
    
    for i, t in enumerate(terms):
        k, v = t.split()
        terms_dict[k] = int(v)
    
    answer = []
    for i, v in enumerate(privacies):
        ds, t = v.split()
        
        limit = to_days(ds, terms_dict[t])
        
        if limit - 1 < todays:
            answer.append(i + 1)
        
    
    
    return answer # 오름차순으로 정렬 후 반환