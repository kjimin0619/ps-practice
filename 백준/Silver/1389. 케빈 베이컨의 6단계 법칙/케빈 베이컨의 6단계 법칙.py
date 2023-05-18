from sys import stdin as s
INF = int(1e9)

n,m = map(int,s.readline().split())
f_net = [[INF]*(n+1) for _ in range(n+1)] # 친구 형성관계망

for _ in range(m):
    f1, f2 = map(int,s.readline().split())
    f_net[f1][f2] = f_net[f2][f1] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            f_net[i][j] = min(f_net[i][j], f_net[i][k] + f_net[k][j])    

# 케빈베이컨 계산
result = [INF]*(n+1)
for i in range(1,n+1):
    f_net[i][0] = f_net[i][i] = 0
    result[i] = sum(f_net[i])
print(result.index(min(result)))