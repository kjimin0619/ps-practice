from sys import stdin as s
from collections import deque

n = int(s.readline())
house = [[] for _ in range(n)]
for i in range(n):
    house[i]= list(map(int, s.readline().strip()))
            
direction = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[False for _ in range(n)]  for _ in range(n)]

dq = deque()
count = []

# BFS
for i in range(n):
    for j in range(n):
        if house[i][j] == 1 and visited[i][j] == False:
            c = 1
            dq.append((i,j))
            while dq :
                curr_x, curr_y = dq.popleft()
                visited[curr_x][curr_y] = True
                    
                for (x, y) in direction :
                    _x, _y = curr_x + x, curr_y  + y
                    if (-1 < _x < n and -1 < _y < n and house[_x][_y] == 1 and visited[_x][_y] == False):
                        dq.append((_x,_y))
                        visited[_x][_y] = True
                        c += 1
            count.append(c)
            
print(len(count))
for i in sorted(count):
    print(i)
