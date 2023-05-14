from sys import stdin as s
from collections import deque

#s = open("input.txt","rt")
N = int(s.readline())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(s.readline().strip())

visited = [[False] * N for _ in range(N)] # 방문 기록
move = [(0,-1),(-1,0),(1,0),(0,1)]
dq = deque()
three_cnt = 0
two_cnt = 0

def bfs(a,b):
    cnt = 0
    dq.append((a,b))
    color = graph[a][b]

    while dq:
        x,y = dq.popleft()
        visited[x][y] = True
        for (i,j) in move:
            new_x = x+i
            new_y = y+j
            if (0<=new_x<N) and (0<=new_y<N):
                if (graph[new_x][new_y] == color and visited[new_x][new_y] != True):
                    visited[new_x][new_y] = True
                    dq.append((new_x,new_y))

# 일반
for i in range(N):
    for j in range(N):
        if (visited[i][j] == False):
            bfs(i,j)
            three_cnt = three_cnt + 1

# 적록색약
for i in range(N):
    for j in range(N):
        visited[i][j] = False # 방문 기록 초기화
        
        # R == G 동일하게 변경
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if (visited[i][j] == False):
            bfs(i,j)
            two_cnt = two_cnt + 1

print(three_cnt, two_cnt)

