from sys import stdin as s
n = int(s.readline().strip())
strong = [] # 내구도
weight = [] # 무게

for _ in range(n) :
    a,b = map(int, s.readline().split())
    strong.append(a)
    weight.append(b)
    
def dfs(now) :
    # 마지막 계란이라면
    if now == n :
        cnt = 0
        for e in strong :
           if e <= 0 :
               cnt += 1
        return cnt
    
    # 현재 계란이 깨진 계란이라면
    if strong[now] <= 0 :
        return dfs(now+1)
    
    # 계란 깰 거 남아있는지 확인하기
    flag = 0
    for i in range(n):
        if i == now :
            continue
        if strong[i] > 0 :
            flag = 1
            break
    if flag == 0 :
        return dfs(now+1) # 깰 거 없음
    
    answer = 0
    for i in range(n):
        if i == now or strong[i] <= 0 :
            continue
        
        strong[i] -= weight[now]
        strong[now] -= weight[i]
        
        answer = max(answer, dfs(now+1))
        
        strong[i] += weight[now]
        strong[now] += weight[i]
    
    return answer

print(dfs(0))