from sys import stdin as s
from collections import deque

def bfs(r,c):
    q = deque()
    graph[r][c] = 0 # 방문처리  
    q.append((r,c))

    while q:
        r,c = q.popleft()
        for dr, dc in direction:
            next_r = r + dr
            next_c = c + dc
            if (0<=next_c<N) and (0<=next_r<N) and (graph[next_r][next_c] == -1):
                q.append((next_r,next_c)) 
                graph[next_r][next_c] = graph[r][c]+ 1

#s = open("input.txt", "rt")
N = int(s.readline().strip()) # 체스판의 크기
r1,c1,r2,c2 = map(int,s.readline().split()) # 시작과 끝 정의

graph = [[-1]*N for _ in range(N)]
direction = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

bfs(r1,c1)
print(graph[r2][c2])