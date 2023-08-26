def solution(book_time):
    cnt = len(book_time)
    # 시간 정수화
    for i in range(cnt):
        start, end = book_time[i]
        start_h = int(start[:2])
        start_m = int(start[3:])
        end_h = int(end[:2])
        end_m = int(end[3:])
        
        book_time[i] = [start_h * 60 + start_m, end_h * 60 + end_m +10]
        
    # 오름차순 정렬    
    book_time = sorted(book_time, key = lambda x : (x[0], x[1]))
    room = []
    
    while book_time :
        cur = book_time.pop(0)
        cur_start, cur_end = cur[0], cur[1]
        flag = False
        if room :
            for r in room :
                last = r[-1]
                exit_time = last[-1]
                if cur_start >= exit_time :
                    r.append(cur)
                    flag = True
                    break
            if flag == False :
                room.append([cur])
                
        else :
            room.append([cur])
    
    answer = len(room)
    return answer