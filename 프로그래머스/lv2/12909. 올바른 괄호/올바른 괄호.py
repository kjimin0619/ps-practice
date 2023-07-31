from collections import deque

def solution(s):
    q = deque([])
    for i in range(len(s)):
        if s[i] == ")":
            if not q :
                return False
            else :
                temp = q.pop()       
        else :
            q.append(s[i])
    if q:
        return False
            
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True