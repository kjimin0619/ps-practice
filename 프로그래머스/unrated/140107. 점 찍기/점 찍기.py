import math

def solution(k, d):
    answer = 0
    a = 0
    while a*k <= d :
        curr = a * k
        y = int(math.sqrt(d*d - curr*curr))
        answer += (y // k +1)
        a += 1
    return answer