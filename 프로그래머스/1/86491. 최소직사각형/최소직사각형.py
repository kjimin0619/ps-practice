def solution(sizes):
    # 재정렬 결과
    newList = []

    # 완전탐색 후 재정렬
    for w, h in sizes:
        newList.append([max(w, h), min(w, h)])
                
    maxW = max(w for w,h in newList)
    maxH = max(h for w,h in newList)
    
    answer = maxW * maxH
    
    return answer