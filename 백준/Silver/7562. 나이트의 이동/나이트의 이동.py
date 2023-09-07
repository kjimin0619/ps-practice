from sys import stdin as s
from collections import deque

test = int(s.readline())

def bfs(start_x, start_y, end_x, end_y, n, q) :
    distance = [[0 for _ in range(n)] for _ in range(n)]
    q.append((start_x, start_y))
    
    while q :
        x,y = q.popleft()
        
        if x == end_x and y == end_y :
            return distance[x][y]
        
        for i,j in [(-1,2),(-2,1),(1,2),(2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)] :
            nx, ny = x + i , y + j
            if 0<=nx<n and 0<=ny<n and distance[nx][ny] == 0 :
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))
    
    
for i in range(test) :
    n = int(s.readline())
    q = deque([])
    s_x, s_y = map(int, s.readline().split())
    e_x, e_y = map(int, s.readline().split())
    print(bfs(s_x, s_y, e_x, e_y, n, q))