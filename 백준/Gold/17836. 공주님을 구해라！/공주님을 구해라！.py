from sys import stdin as s
from collections import deque

N,M,T = map(int, s.readline().split())
board = []
for i in range(N) :
    board.append(list(map(int, s.readline().split())))
    if 2 in board[i] :
        g_x, g_y = i, board[i].index(2) # 그람 위치저장
        
def bfs(s_x, s_y, e_x, e_y, time) :
    visited = [[False for _ in range(M)] for _ in range(N)] 
    q = deque([(s_x, s_y, time)])
    
    while q :
        x,y, time = q.popleft()
        visited[x][y] = True
        for i, j in [(-1,0),(0,1),(0,-1),(1,0)] :
            x_ = x + i
            y_ = y + j
            
            if (0 <= x_ <N and 0 <= y_ < M and not visited[x_][y_] and board[x_][y_] != 1) :
                visited[x_][y_] = True
                
                if x_ == e_x and y_ == e_y :
                    return (time+1)
                
                q.append((x_,y_,time+1))

    return float('inf')

# 그람 안 쓸 때 
no_gram = bfs(0,0,N-1,M-1,0)

# 그람 쓸 때 
gram = bfs(0,0,g_x, g_y,0) 
if gram != float('inf'):
    gram = gram + abs(N-1 - g_x) + abs(M-1 - g_y)

ans = min(no_gram, gram)
print(ans if ans <= T else 'Fail')