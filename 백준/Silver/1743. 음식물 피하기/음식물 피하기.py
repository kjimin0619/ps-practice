from sys import stdin as s
from collections import deque

#s = open("input.txt","rt")

n,m,k = map(int,s.readline().split())
visited = [[False] * (m+1) for _ in range(n+1)]
g = [[False] * (m+1) for _ in range(n+1)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(k):
    a,b = map(int, s.readline().split())
    g[a][b] = True


def bfs(r,c):
    q = deque()
    q.append((r,c))
    t_cnt = 1
    while q:
        x,y = q.popleft()

        for x_, y_ in direction:
            new_x = x + x_
            new_y = y + y_
            if (0<=new_x<=n and 0<=new_y<=m):
                if visited[new_x][new_y] == False and g[new_x][new_y] == True:
                    t_cnt += 1
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))
    return t_cnt

result = []
for i in range(n+1):
    for j in range(m+1):
        if visited[i][j] != True and g[i][j] == True:
            visited[i][j] = True

            result.append(bfs(i,j))

print(max(result))


