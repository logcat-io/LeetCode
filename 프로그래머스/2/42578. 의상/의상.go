func solution(clothes [][]string) int {
    d := make(map[string]int)

    for _, v := range clothes {
        _, ok := d[v[1]]
        if ok {
            d[v[1]] += 1
        }else {
            d[v[1]] = 1
        }
    }
    
    ans := 1
    for _, v := range d {
        ans *= v + 1
    }
        
    return ans - 1
}