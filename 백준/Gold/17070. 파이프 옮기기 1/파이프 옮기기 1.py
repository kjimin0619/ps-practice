from sys import stdin as s
n = int(s.readline().strip())
board = []
for _ in range(n):
    board.append(list(map(int, s.readline().split())))
    
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

# 가로 첫 번째 행 처리
dp[0][0][1] = 1
for j in range(2,n) :
    if  board[0][j] == 0 :
        dp[0][0][j] = dp[0][0][j-1]

def sol() :
    for i in range(1,n) :
        for j in range(1,n) :
            # 현재 칸이 벽이 아니라면
            if board[i][j] == 0 :
                # 가로 (0) : 가로 + 대각선
                dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1] 
                            
                # 대각선 (1) : 가로 + 대각선
                if board[i][j-1] == 0 and board[i-1][j] == 0:
                    dp[1][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
                
                # 세로 (2) : 세로 + 대각선
                dp[2][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
    
sol()
 
# 최종 답안   
print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])