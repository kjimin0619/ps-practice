from collections import deque


def solution(board):
    n = len(board)
    m = len(board[0])
    
    q = deque()
    d = [[987654321 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R" :
                q.append((i,j,0))
                d[i][j] = 0
                break
  
    while q:
        x,y,c = q.popleft()
        if board[x][y] == "G" :
            return c
        
        for (dx, dy) in [(0,1),(0,-1), (1,0),(-1,0)]:
            _x = x
            _y = y
        
            while (0<=_x+dx<n and 0<=_y+dy < m and board[_x+dx][_y+dy] != "D") :
                _x, _y = _x+dx, _y+dy
            if d[_x][_y] > c+1 :
                d[_x][_y] = c+1
                q.append((_x,_y,c+1))
  
    return -1