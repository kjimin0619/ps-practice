# 2583 영역 구하기
import sys
from collections import deque

m, n, k = map(int, input().split())
paper = [[0] * n for _ in range(m)]  # 0 : 직사각형 없음
d = deque([])
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visited = [[0] * n for _ in range(m)]


def bfs(i, j):
  d.append((i, j))
  ans = 1
  while d:
    cx, cy = d.popleft()
    visited[cx][cy] = 1

    for di, dj in direction:
      nx = di + cx
      ny = dj + cy

      if (0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0
          and paper[nx][ny] == 0):
        ans += 1
        visited[nx][ny] = 1
        d.append((nx, ny))

  return ans


# 직사각형 만들기
for _ in range(k):
  startX, startY, endX, endY = map(int, sys.stdin.readline().split())
  for i in range(startY, endY):
    for j in range(startX, endX):
      paper[i][j] = 1

# 영역 탐색
total = []
for i in range(m):
  for j in range(n):
    if paper[i][j] == 0 and visited[i][j] == 0:
      ans = bfs(i, j)  # 분리된 영역 계산
      total.append(ans)

total.sort()
print(len(total))
print(*total)
