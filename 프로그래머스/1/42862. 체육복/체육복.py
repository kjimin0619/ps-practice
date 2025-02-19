def solution(n, lost, reserve):
    answer = 0
    for i in range(1,n+1) :
        # 도난 당한 학생이다
        if i in lost :
            # 그런데 내가 여벌 체육복이 있다
            if i in reserve :
                answer +=1 
            # 내가 여벌 체육복이 없어서 빌려야 한다
            else :
                for j in range(i-1,i+2):
                    if j in reserve and j not in lost :
                        answer += 1
                        reserve.remove(j)
                        break
                
        # 도난 당하지 않았다
        else :
            answer += 1
    
    return answer