def solution(mats, park):
    n = len(park)
    m = len(park[0])
    answer = -1
    
    for i in range(n):
        for j in range(m):
            if park[i][j] != "-1":
                continue
            
            for a in mats:
                no = False
                if i +  a > n or j + a > m: continue
                
                for k in range(i, i+a):
                    for w in range(j, j+a):
                        if park[k][w] != "-1":
                            no = True
                            break
                    if no: break
                if not no: answer = max(answer, a)

    return answer