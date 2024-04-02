# 14442 벽 부수고 이동하기 2
from collections import deque
import sys

n, m, k = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]

visited[0][0][0] = 1
d = deque([(0, 0, 0)])
flag = 0

while d:
  ck, cn, cm = d.popleft()
  # 도착했다면?
  if cn == n - 1 and cm == m - 1:
    flag = 1
    print(visited[ck][cn][cm])
    break

  # 이동
  for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    nn, nm = dy + cn, dx + cm

    if (0 <= nn < n and 0 <= nm < m):
      # 일반 이동
      if visited[ck][nn][nm] == 0 and graph[nn][nm] == 0:
        visited[ck][nn][nm] = visited[ck][cn][cm] + 1
        d.append((ck, nn, nm))

      # 벽 부수고 이동
      elif (ck < k and graph[nn][nm] == 1 and visited[ck + 1][nn][nm] == 0):
        visited[ck + 1][nn][nm] = visited[ck][cn][cm] + 1
        d.append((ck + 1, nn, nm))

if not flag:
  print(-1)
