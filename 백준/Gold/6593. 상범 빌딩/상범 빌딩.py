# 6593 상범 빌딩
import sys
from collections import deque

while True:
  L, R, C = map(int, input().split())
  if L == 0 and R == 0 and C == 0:
    break

  building = []
  d = deque([])
  timer = 0  # 탈출 소요 시간
  flag = 0  # 탈출 여부
  visited = [[[0] * C for _ in range(R)] for _ in range(L)]
  direction = [(0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0), (0, 1, 0),
               (0, -1, 0)]

  # 빌딩 정보 입력
  for h in range(L):
    hTemp = []
    for i in range(R):
      temp = list(map(str, sys.stdin.readline().strip()))
      hTemp.append(temp)

      for j in range(C):
        if temp[j] == 'S':
          d.append((h, i, j))
          visited[h][i][j] = 1

    building.append(hTemp)
    blank = input()

  # 탐색 bfs
  while d:
    for _ in range(len(d)):
      l, r, c = d.popleft()

      if building[l][r][c] == 'E':
        flag = 1
        d = []
        break

      for dl, dr, dc in direction:
        nl, nr, nc = l + dl, r + dr, c + dc
        if (0 <= nl < L and 0 <= nr < R and 0 <= nc < C
            and visited[nl][nr][nc] == 0 and building[nl][nr][nc] != '#'):
          visited[nl][nr][nc] = 1
          d.append((nl, nr, nc))

    timer += 1

  if flag:
    print("Escaped in {} minute(s).".format(timer - 1))
  else:
    print("Trapped!")
