from sys import stdin as s
from collections import deque

n = int(s.readline()) # 노드의 수
parent = [0]*(n+1)
g = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent[1] = 1 # 트리의 루트는 1 
dq = deque()

# 연결 그래프 
for i in range(n-1):
    a,b = map(int, s.readline().split())
    g[a].append(b)
    g[b].append(a)

# bfs
dq.append(1)
visited[1] = True
while(dq):
    a = dq.popleft()
    visited[a] = True
    for son in g[a]:
        if visited[son] == False :
            dq.append(son)
            parent[son] = a

for i in range(2,n+1):
    print(parent[i])