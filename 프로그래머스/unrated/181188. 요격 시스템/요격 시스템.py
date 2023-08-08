def solution(targets):
    targets = sorted(targets, key = lambda x : x[1]) # e 기준 오름차순 정렬
    
    limit = -1
    cnt = 0
    
    for target in targets :
        if target[0] > limit :
            limit = target[1] - 0.1
            cnt += 1
    
    return cnt

