def solution(k, ranges):
    answer = []
    numbers = []
    # 우박수열 찾기
    i = k
    numbers.append(i)
    while i != 1 :
        if i%2 == 0 :
            i = i // 2
        else :
            i = i * 3 + 1
        numbers.append(i)
    
    # 정적분
    n = len(numbers) - 1
    
    for s, e in ranges :
        start = s
        end = n + e
     
        if start > end :
            result = -1
        else :
            result = 0
            for i in range(start, end):
                under_rec = 1 * numbers[i]
                high_tri = (numbers[i+1] - numbers[i]) / 2
                result = result + under_rec + high_tri
            
        answer.append(result)
    return answer