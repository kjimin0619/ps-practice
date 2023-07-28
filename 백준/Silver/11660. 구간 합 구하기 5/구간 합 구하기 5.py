from sys import stdin as s

n,m = map(int,s.readline().split())

board = []
for _ in range(n):
    board.append(list(map(int,s.readline().split())))

# (0,0)부터 (x,y)까지의 모든 부분합 구하기
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        elif i == 0 :
            board[i][j] += board[i][j-1]
        elif j == 0 :
            board[i][j] += board[i-1][j]
        else:
            board[i][j] = (board[i][j] + board[i-1][j] 
                        + board[i][j-1] - board[i-1][j-1])
    
# 주어진 범위의 부분합 구하기
for _ in range(m):
    result  = 0
    x, y, a, b = map(int, s.readline().split())
    x -= 1
    y -= 1
    a -= 1
    b -= 1

    if (x == 0 and y == 0):
        result = board[a][b]

    elif (x > 0 and y > 0):
        result = (board[a][b] - board[x-1][b] 
              - board[a][y-1] + board[x-1][y-1] )
    else :
        if x == 0 :
            result = (board[a][b] - board[a][y-1])
        else :
            # y == 0
            result = (board[a][b] - board[x-1][b]) 
    
    print(result)