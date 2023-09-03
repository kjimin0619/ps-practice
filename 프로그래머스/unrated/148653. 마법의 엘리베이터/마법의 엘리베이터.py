import math
def solution(storey):
    answer = 0
    while storey > 0 :
        storey, rest = divmod(storey, 10)
        if rest > 5 or (rest == 5 and storey%10 >= 5) :
            rest = 10 - rest
            storey += 1
        answer += rest
    return answer