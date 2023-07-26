from sys import stdin as s

t = int(s.readline().strip()) # 테스트 케이스 갯수

def solve(board, n):
    dp = [[0] * n for _ in range(2)]
    if n == 1 :
        dp[0][0] = board[0][0]
        dp[1][0] = max(board[0][0], board[1][0])
        return dp

    dp[0][0] = board[0][0]
    dp[1][0] = max(board[1][0], board[0][0])
    dp[0][1] = max(board[0][1]+board[1][0],
                            board[0][0])
    dp[1][1] = max(board[0][1]+board[1][0],
                            board[1][1]+board[0][0])

    for j in range(2,n):
        # 윗 줄
        dp[0][j] = max(
            dp[1][j-1], # 본인 x
            board[0][j] + dp[1][j-2], # 본인 o 대각선 x
            board[0][j] + board[1][j-1] + dp[0][j-2] # 본인 o 대각선 o
        )
        # 아랫줄 
        dp[1][j] = max(
            dp[0][j], # 본인 x
            board[1][j] + dp[0][j-1] # 본인 o
        )
    return dp


for _ in range(t):
    n = int(s.readline().strip()) 

    board = []
    board.append(list(map(int,s.readline().split()))) # 1행
    board.append(list(map(int,s.readline().split()))) # 2행
    res = solve(board, n)
    print(res[1][n-1])


        
