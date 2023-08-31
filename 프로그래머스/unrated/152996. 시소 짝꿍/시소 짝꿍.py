def solution(weights):
    dist = [0] * 100001
    
    answer= 0
    weights_kind = set(weights)
    for w in  weights_kind :
        cnt = weights.count(w)
        print(w, cnt)
        # 1 : 1
        if w >= 2 :
            answer += (cnt * (cnt - 1) / 2)
        
        # 2 : 3
        cnt_23 = weights.count(w*(3/2))
        if cnt_23 > 0 :
            answer += cnt * cnt_23
        
        # 2 : 4
        cnt_24 = weights.count(w*2)
        if cnt_24 > 0 :
            answer += cnt * cnt_24
            
        # 3 : 4
        cnt_34 = weights.count(w*(4/3))
        if cnt_34 > 0 :
            answer += cnt * cnt_34
    
    return answer