from sys import stdin as s
from collections import deque

r,c = map(int,s.readline().split())

direction = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
visited = [[False]*c for _ in range(r)]
yard = [[] *c for _ in range(r)]

for i in range(r):
    yard[i] = list(s.readline().strip())

def bfs(x,y):
    q = deque()
    q.append((x,y))
    wolf = 0 
    sheep = 0

    while (q):
        x,y = q.popleft()

        for (x_,y_) in direction:
            new_x, new_y = x + x_, y + y_
            if (yard[new_x][new_y] == '#'):
                continue
            elif (0<=new_x<r and 0<=new_y<c and visited[new_x][new_y] != True):
                q.append((new_x,new_y))
                visited[new_x][new_y] = True
                if yard[new_x][new_y] == 'v':
                    wolf += 1
                elif yard[new_x][new_y] == 'o':
                    sheep += 1

    # 특정 영역 안에 있는 늑대와 양 수 계산 완료 후
    if (sheep > wolf):
        return (sheep, 0)
    else :
        return (0, wolf)

v = o = 0 
for i in range(r):
    for j in range(c):
       if(yard[i][j] != '#' and yard[i][j] != '.' ):
            (s,w)= bfs(i,j)
            v += w
            o += s
print(o,v)

