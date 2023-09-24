from sys import stdin as s
n = int(s.readline().strip())

board = []
for i in range(n) :
    board.append(list(map(int, s.readline().split())))
    

total = 0
# pos : 가로 0 세로 1 대각선 2
def dfs(x,y, pos) :
    global total
    
    if x == n-1 and y == n-1 :
        total += 1
        return
    
    # 대각선 이동
    if x+1 < n and y+1 < n and board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
        dfs(x+1, y+1,2)
        
    # 가로
    if pos == 0 or pos == 2:
        if x < n and y+1 < n and board[x][y+1] == 0 :
            dfs(x,y+1,0)

    # 세로
    if pos == 1 or pos == 2 :
        if y < n and x+1 < n and board[x+1][y] == 0 :
            dfs(x+1,y,1)
    
# 시작
dfs(0, 1, 0)
print(total)