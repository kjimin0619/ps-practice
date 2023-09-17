def solution(order):
    answer = []
    stack = []
    
    c = 1
    t = 0
    while t < len(order):
        if c == order[t] :
            answer.append(order[t])
            c += 1
            t += 1
            
        elif stack and stack[-1] == order[t] :
                stack.pop(-1)
                answer.append(order[t])
                t += 1
           
        else :
            while c < len(order)+1 and c != order[t]:
                stack.append(c)
                c += 1

            if c == order[t] :
                answer.append(order[t])
                t += 1
                c += 1
                
            else : break
              

    return len(answer)