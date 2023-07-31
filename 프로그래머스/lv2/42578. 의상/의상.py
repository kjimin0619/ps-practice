
def solution(clothes):
    closet = {} 
    for name, category in clothes :
        if category in closet :
            closet[category] += 1
        else :
            closet[category] = 1
    all_values = closet.values()
    answer= 1
    for k in all_values:
        answer = answer * (k+1)
        
    return answer-1