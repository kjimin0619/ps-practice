from sys import stdin as s

n = int(s.readline()) # 수열의 크기
a = list(map(int, s.readline().split())) # 전체 수열
dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if a[i] > a[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

