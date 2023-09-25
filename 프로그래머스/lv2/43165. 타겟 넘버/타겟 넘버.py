from collections import deque
def solution(numbers, target):
    q = deque([0])
    answer = 0

    for i in range(len(numbers)) :
        for j in range(2**(i)) :
            cur = q.popleft()
            temp1 = cur+numbers[i]
            temp2 = cur-numbers[i]
            q.append(temp1)
            q.append(temp2)
    
    while q :
        if q.popleft() == target :
            answer += 1
    return answer

