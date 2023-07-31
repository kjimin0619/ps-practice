def solution(seoul):
    answer = ''
    pos = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            pos = i
            
    answer = "김서방은 {}에 있다".format(pos)
    return answer