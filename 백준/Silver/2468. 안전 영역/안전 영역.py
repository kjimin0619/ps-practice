# 2468 안전영역
import sys
from collections import deque

n = int(input())
ground = []
maxH = 0  # 최대 높이
ans = 0  # 답
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(n):
  temp = list(map(int, sys.stdin.readline().split()))
  if max(temp) > maxH:
    maxH = max(temp)
  ground.append(temp)

# 안전 영역 탐색
for h in range(maxH):
  visited = [[0] * n for _ in range(n)]
  cnt = 0  # 안전 영역 갯수
  d = deque([])

  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0 and ground[i][j] > h:
        visited[i][j] = 1
        cnt += 1
        d.append((i, j))

        while d:
          cx, cy = d.popleft()

          for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if (0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0
                and ground[nx][ny] > h):
              d.append((nx, ny))
              visited[nx][ny] = 1

  # 안정 영역 개수 비교
  if ans < cnt:
    ans = cnt

print(ans)
