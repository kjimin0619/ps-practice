from sys import stdin as s
from collections import deque

n,m = map(int, s.readline().split())
maps = []
for i in range(n):
    temp = map(int,s.readline().strip())
    maps.append(list(temp))


distance = [[0 for _ in range(m)] for _ in range(n)]
q = deque([(0,0)])
distance[0][0] = 1

while q :
    x,y = q.popleft()
    
    if x == n-1 and y == m-1 :
        print(distance[x][y])
        break
    
    for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx, ny = x+i, y+j
        
        if 0<=nx<n and 0<=ny<m and distance[nx][ny] == 0 and maps[nx][ny] == 1 :
            distance[nx][ny] = distance[x][y] + 1            
            q.append((nx,ny))