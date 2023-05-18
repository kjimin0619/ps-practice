from sys import stdin as s

n,m = map(int,s.readline().split())
f_net = [[] for _ in range(n+1)] # 친구 형성관계망

for _ in range(m):
    f1, f2 = map(int,s.readline().split())
    f_net[f1].append(f2)
    f_net[f2].append(f1)

from collections import deque

def bfs(start):
    cnt = [0] * (n+1)
    visited[start] = 1
    q = deque()

    q.append(start)

    while q:
        now = q.popleft()

        for nodes in f_net[now]:
            if visited[nodes] == 0 :
                cnt[nodes] = cnt[now] + 1
                q.append(nodes)
                visited[nodes] = 1
    return sum(cnt)

result = []
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    result.append(bfs(i))

print(result.index(min(result))+1)