from sys import stdin as s
n = int(s.readline().strip())

# 경로 정보 저장
board = []
for _ in range(n):
    board.append(list(map(int,s.readline().split())))
        
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1 :
            print(dp[i][j])

        step = board[i][j]
        # 옆으로 이동
        if j + step < n :
            dp[i][j+step] += dp[i][j]
        
        # 아래로 이동
        if i + step < n :
            dp[i+step][j] += dp[i][j]