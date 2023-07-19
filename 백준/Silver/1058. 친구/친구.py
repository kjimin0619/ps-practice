from sys import stdin as s
from collections import deque

n = int(s.readline())
friend2 = []
graph = [[]]

for i in range(n):
    f = list(s.readline().strip())
    graph.append([i+1 for i in range(n) if f[i] == 'Y'])

# bfs - queue
def bfs(k):
    q = deque()
    q.append(k)
    i = 0
    visited = [False] * (n+1)
    visited[k] = True
    
    for frnd in graph[k] :
        visited[frnd] = True
        i+=1
        q.append(frnd)

    while q :
        n_curr = q.popleft()
        visited[n_curr] = True
        for frnd in graph[n_curr] :
            if (visited[frnd] == False):
                visited[frnd] = True
                i+=1
    friend2.append(i)
            
for i in range(1,n+1):
    bfs(i)

print(max(friend2))