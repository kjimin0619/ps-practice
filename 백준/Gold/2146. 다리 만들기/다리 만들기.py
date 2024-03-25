import sys
from collections import deque

ans = int(1e9)

n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
inum = 2  # 대륙 번호
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def bfs(i, j):
  d = deque([(i, j)])
  while d:
    cx, cy = d.popleft()
    for dx, dy in direction:
      nx, ny = cx + dx, cy + dy
      if (0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1):
        d.append((nx, ny))
        graph[nx][ny] = inum


def calPath(inum):
  path = [[-1] * n for _ in range(n)]
  d = deque([])
  for i in range(n):
    for j in range(n):
      if graph[i][j] == inum:
        path[i][j] = 0
        d.append((i, j))

  while d:
    cx, cy = d.popleft()
    for dx, dy in direction:
      nx, ny = cx + dx, cy + dy
      if (0 <= nx < n and 0 <= ny < n):
        if graph[nx][ny] == 0 and path[nx][ny] == -1:  # 바다
          path[nx][ny] = path[cx][cy] + 1
          d.append((nx, ny))
        elif graph[nx][ny] and graph[nx][ny] != inum:
          # 타대륙 도작
          return path[cx][cy]

  return 1e9


for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      graph[i][j] = inum
      bfs(i, j)
      inum += 1

for num in range(2, inum):
  ans = min(ans, calPath(num))

print(ans)
