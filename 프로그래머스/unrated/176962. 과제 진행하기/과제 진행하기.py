def solution(plans):
    # 시간 분 단위 숫자화 후 오름차순 정렬
    for i in plans:
        time = i[1]
        hour = int(time[:2])
        minute = int(time[3:])
        i[1] = 60*hour + minute
        i[2] = int(i[2])
    plans = sorted(plans, key = lambda x : x[1]) 
    
    
    stack = [] # 일시 중단된 과목들
    fin = [] # 수행 완료된 과목들
    i = 0
    time = plans[0][1] # 시작 시간
    
    # 새 작업들 시간 순서대로 수행하기
    while i < len(plans) :
        cur = plans[i]
        cur_start_time = cur[1]
        cur_end_time = cur[1] + cur[2]
        if i+1 == len(plans) :
            next_start_time = 60*24 # 최대값
        else :
            next_start_time = plans[i+1][1]
        
        # 현재 과목 시작가능한 시간이 아니라면
        if time < cur_start_time :
            # 스택안의 과제가 존재할 때
            if stack :
                name, left_time = stack.pop()
                # 끝낼 수 있다면
                if time + left_time <= cur_start_time :
                    fin.append(name)
                    time = time + left_time

                # 끝낼 수 없다면
                else :
                    duration = cur_start_time - time
                    stack.append((name, left_time - duration)) # 가능한만큼만 하고 다시 넣기
                    time = cur_start_time
                    
            # 스택안의 과제가 없다면 현재 과제 바로 시작
            else :
                time = cur_start_time

        # 다음 과목 시작전까지 현재 과목을 끝낼 수 있다면
        elif (cur_end_time <= next_start_time) : 
            fin.append(cur[0])
            i += 1
            time = cur_end_time 
            
        # 현재 과목을 중단해야 한다면
        elif (cur_end_time > next_start_time) :
            left_time = cur[2] - (next_start_time - cur_start_time)
            stack.append((cur[0], left_time))
            time = next_start_time
            i += 1
            
        
    #남은 스택 비우기
    while stack:
        temp = stack.pop()
        fin.append(temp[0])
        
    return fin