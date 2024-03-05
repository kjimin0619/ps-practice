# 7569 토마토
import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())  # 가로, 세로, 높이
box = []  # 전체 토마토를 담을 상자. 1 익음 / 0 안익음 / -1 토마토 없음
visited = [[[0] * m for _ in range(n)] for _ in range(h)]  # 방문 여부
d = deque([])  # 큐


def bfs(day):
  # 토미토 정보 저장
  for i in range(h):
    temp = []
    for j in range(n):
      tomatoes = list(map(int, sys.stdin.readline().split()))
      temp.append(tomatoes)
      # 익은 토마토 저장
      for k in range(m):
        if temp[j][k] == 1:
          d.append((i, j, k))
          visited[i][j][k] = 1
    box.append(temp)

  # 토마토 확산 방향
  direction = [(0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0),
               (-1, 0, 0)]

  # 토마토 익기 시작
  while d:
    for _ in range(len(d)):
      i, j, k = d.popleft()

      # 토마토 확산
      for x, y, z in direction:
        ni, nj, nk = i + x, j + y, k + z
        if (0 <= ni < h and 0 <= nj < n and 0 <= nk < m
            and box[ni][nj][nk] == 0 and visited[ni][nj][nk] == 0):
          box[ni][nj][nk] = 1
          visited[ni][nj][nk] = 1
          d.append((ni, nj, nk))

    day += 1  # 하루 경과

  return day - 1


def checkBox(day):
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if box[i][j][k] == 0:
          print(-1)
          return

  print(day)


day = 0
day = bfs(day)
checkBox(day)
