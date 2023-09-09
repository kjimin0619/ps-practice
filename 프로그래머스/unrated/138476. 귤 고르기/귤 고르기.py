def solution(k, tangerine):
    # 개수 세기
    cnt_type = {}
    for t in tangerine :
        if t in cnt_type :
            cnt_type[t] += 1
        else :
            cnt_type[t] = 1
            
    counts = sorted(cnt_type.values(),key= lambda x : -x)
    
    i = 0
    while k > 0 and i < len(counts):
        cur = counts[i]
        k -= cur
        i += 1
   
    return i