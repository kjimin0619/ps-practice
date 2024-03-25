from collections import deque
import sys

d = deque([1])

n = int(input().strip())
cpl = int(input().strip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(cpl):
  n1, n2 = map(int, sys.stdin.readline().split())
  graph[n1].append(n2)
  graph[n2].append(n1)

cnt = 0
while d:
  cur = d.popleft()
  visited[cur] = True
  for nxt in graph[cur]:
    if not visited[nxt]:
      visited[nxt] = True
      cnt += 1
      d.append(nxt)

print(cnt)
