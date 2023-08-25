from collections import deque

def solution(board) :
    m = len(board[0])
    n = len(board)
    
    for i in range(n) :
        for j in range(m):
            if board[i][j] == "R":
                s_x, s_y = i, j
                q = deque((s_x, s_y, 0))    
                break
                
    # 탐색 시작 bfs
    q = deque([(s_x, s_y, 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[s_x][s_y] = True
    
    while q :
        x,y, cnt = q.popleft()
        if board[x][y] == "G" :
            return cnt
        
        for i,j in [(0,1),(0,-1), (1,0),(-1,0)]:
            _x, _y = x, y

            while (0 <= _x+i < n and 0 <= _y+j < m) and board[_x+i][_y+j] != "D" :
                _x += i
                _y += j
            
            if not visited[_x][_y] :
                visited[_x][_y] = True
                q.append((_x, _y, cnt+1))
                
    return -1
            