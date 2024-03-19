# 2206 벽 부수고 이동하기
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
board = []
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
d = deque([(0, 0, 0)])
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
flag = 0

# 행렬 맵 정보 받기
for _ in range(n):
  temp = list(sys.stdin.readline().strip())
  board.append(temp)

# bfs
visited[0][0][0] = 1  # 시작지점 방문처리

while d:
  cn, cm, cw = d.popleft()  # 현 위치

  # 목표 지점 도달
  if cn == n - 1 and cm == m - 1:
    print(visited[cn][cm][cw])
    flag = 1
    break

  for dn, dm in direction:
    nn, nm = cn + dn, cm + dm

    if (0 <= nn < n and 0 <= nm < m):
      # 첫 방문에다가 지나갈 수 있다면
      if board[nn][nm] == '0' and visited[nn][nm][cw] == 0:
        visited[nn][nm][cw] = visited[cn][cm][cw] + 1
        d.append((nn, nm, cw))

      # 첫 방문이지만 벽이고, 아직 벽 부수지 않았다면
      elif board[nn][nm] == '1' and cw == 0:
        visited[nn][nm][1] = visited[cn][cm][cw] + 1
        d.append((nn, nm, 1))

if flag == 0:
  print(-1)
