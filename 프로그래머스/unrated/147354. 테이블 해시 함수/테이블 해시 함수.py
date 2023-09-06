def solution(data, col, row_begin, row_end):
    # 정렬
    sorted_data = sorted(data, key = lambda x : (x[col-1], -x[0]))
    
    res = 0
    for i in range(row_begin, row_end+1 ) :
        total = 0
        
        for j in sorted_data[i-1]:
            total += (j % i)
        res = res ^ total
    
    
    return res