from sys import stdin as s

n, k = map(int, s.readline().split())
weights = []
values = []

for _ in range(n) :
    w,v = map(int, s.readline().split())
    weights.append(w)
    values.append(v)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, k+1):
        if j >= weights[i-1]:
            dp[i][j] = max(dp[i-1][j], 
                           values[i-1] + dp[i-1][j - weights[i-1]] )
        else :
            dp[i][j] = dp[i-1][j]
print(dp[n][k])