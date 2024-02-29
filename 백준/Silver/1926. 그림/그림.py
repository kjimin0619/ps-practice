# bfs -> 큐, dfs -> stack & 재귀
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 이동 가능 방향
visited = [[False for _ in range(m)] for _ in range(n)]

# graph 채우기
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

# bfs
total = []
for i in range(n):
  for j in range(m):
    if graph[i][j] and not visited[i][j]:
      currentSize = 1  # 그림의 넓이
      d = deque([(i, j)])
      visited[i][j] = True  # 방문 처리

      while d:
        x, y = d.popleft()

        for dx, dy in direction:
          nx, ny = x + dx, y + dy
          if 0 <= nx and nx < n and 0 <= ny and ny < m and graph[nx][ny]:
            if not visited[nx][ny]:
              visited[nx][ny] = True
              d.append((nx, ny))
              currentSize += 1

      total.append(currentSize)

print(len(total))
if total :
  print(max(total))
else :
  print("0")
