def solution(sequence, k):
    answer = []
    start, end = 0,0
    temp = sequence[0]
    min_len = 1000001
    limit = len(sequence)
    
    while start <= end < limit:
        if temp == k :
            if end - start + 1 < min_len :
                min_len = end - start + 1
                answer = [start, end]
            temp -= sequence[start]
            start += 1
            
        elif temp < k :
            end += 1
            if end < limit :
                temp += sequence[end]
                
        elif temp > k :
            temp -= sequence[start]
            start += 1
    
    return answer