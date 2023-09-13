from sys import stdin as s
from collections import deque

t = int(s.readline())

def bfs(x,y, board, visited):
    q = deque([(x,y)])
    
    while q :
        cx, cy = q.popleft()
        visited[cx][cy] = True
        
        for i,j in [(-1,0),(0,1),(1,0),(0,-1)]:
            nx, ny = cx + i, cy +j
            
            if 0 <= nx <m and 0 <= ny < n and visited[nx][ny] == False and board[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny))
                
for _ in range(t) :  
    m, n, k = map(int, s.readline().split())
    board = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]             
    for _ in range(k):
        i,j = map(int, s.readline().split())
        board[i][j] = 1
    count = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == False and board[i][j] == 1 :
                bfs(i,j, board, visited)
                count += 1
    print(count)