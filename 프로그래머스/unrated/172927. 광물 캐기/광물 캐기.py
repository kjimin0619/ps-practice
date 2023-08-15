import math
def solution(picks, minerals):
    answer = 0
    total_minerals = sum(picks) * 5 # 곡괭이로 캘 수 있는 광물의 수
    
    if (len(minerals) > total_minerals) :
        minerals= minerals[:total_minerals]
        
    # 그룹별 광물조사(5개씩)
    grp_mineral= [[0,0,0] for _ in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            grp_mineral[i//5][0] += 1
        elif minerals[i] == 'iron': 
            grp_mineral[i//5][1] += 1
        else : 
            grp_mineral[i//5][2] += 1
    
    
    grp_mineral = sorted(grp_mineral, key=lambda x : (-x[0], -x[1], -x[2]))
    
    for grp in grp_mineral :
        d, i, s = grp
        
        # 광물 캐기
        for p in range(len(picks)) :
            if p == 0 and picks[p] > 0 :
                picks[p] -= 1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0: 
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0: 
                picks[p]-=1
                answer += 25*d + 5*i + s
                break
                        
    return answer