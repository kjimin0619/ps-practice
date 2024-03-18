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
visited[0][0][0] = 1
while d:
  cn, cm, w = d.popleft()

  # 목적지 도착
  if (cn == n - 1 and cm == m - 1):
    flag = 1
    print(visited[n - 1][m - 1][w])
    break

  # 다음 이동 탐색
  for dn, dm in direction:
    nn, nm = dn + cn, dm + cm

    if (0 <= nn < n and 0 <= nm < m):

      # 다음 이동이 벽이 아니라면
      if board[nn][nm] == '0' and visited[nn][nm][w] == 0:
        visited[nn][nm][w] = visited[cn][cm][w] + 1
        d.append((nn, nm, w))

      # 다음 이동이 벽인데 아직 부수지 않았다면
      elif w == 0 and board[nn][nm] == '1':
        visited[nn][nm][1] = visited[cn][cm][w] + 1
        d.append((nn, nm, 1))

if not flag:
  print(-1)
