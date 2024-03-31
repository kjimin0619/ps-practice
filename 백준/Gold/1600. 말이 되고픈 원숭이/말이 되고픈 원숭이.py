# 1600
from collections import deque

k = int(input().strip())
w, h = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0 for _ in range(w)] for _ in range(h)] for _ in range(k + 1)]

d = deque([])
d.append((0, 0, 0))
visited[0][0][0] = 1
flag = 0

while d:
  tempK, x, y = d.popleft()

  if y == h - 1 and x == w - 1:
    print(visited[tempK][y][x] - 1)
    flag = 1
    break

  # 원숭이 이동
  for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    nx, ny = dx + x, dy + y
    if (0 <= nx < w and 0 <= ny < h and visited[tempK][ny][nx] == 0
        and board[ny][nx] == 0):
      visited[tempK][ny][nx] = visited[tempK][y][x] + 1
      d.append((tempK, nx, ny))

  # 말처럼 이동
  if tempK < k:
    for dx, dy in [(-2, 1), (2, 1), (1, -2), (1, 2), (2, -1), (-2, -1),
                   (-1, 2), (-1, -2)]:
      nx, ny = dx + x, dy + y
      if (0 <= nx < w and 0 <= ny < h and visited[tempK + 1][ny][nx] == 0
          and board[ny][nx] == 0):
        visited[tempK + 1][ny][nx] = visited[tempK][y][x] + 1
        d.append((tempK + 1, nx, ny))

if not flag:
  print(-1)
