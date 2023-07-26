from sys import stdin as s

t = int(s.readline().strip()) # 테스트 케이스 갯수

def solve(board, n):
    dp = [[0] * n for _ in range(2)]
    # j : 열
    for j in range(n):
        # i : 행
        for i in range(2):
            if i == 0 and j == 0 :
                dp[i][j] = board[i][j]
            elif i == 0 and j == 1 :
                dp[i][j] = max(board[0][1]+board[1][0],
                               board[0][0])
            elif i == 1 and j == 0 :
                dp[i][j] = max(board[1][0], board[0][0])
            elif i == 1 and j == 1 :
                dp[i][j] = max(board[0][1]+board[1][0],
                               board[1][1]+board[0][0])
            else :
                if i == 0 :
                    # 윗 줄
                    dp[i][j] = max(
                        dp[1][j-1], # 본인 x
                        board[i][j] + dp[1][j-2], # 본인 o 대각선 x
                        board[i][j] + board[1][j-1] + dp[i][j-2] # 본인 o 대각선 o
                    )
                else :
                    # 아랫줄 
                    dp[i][j] = max(
                        dp[0][j], # 본인 x
                        board[i][j] + dp[0][j-1] # 본인 o
                    )
    return dp


for _ in range(t):
    board = []
    n = int(s.readline().strip()) 
    board.append(list(map(int,s.readline().split())))
    board.append(list(map(int,s.readline().split())))
    res = solve(board, n)
    print(res[1][n-1])


        
