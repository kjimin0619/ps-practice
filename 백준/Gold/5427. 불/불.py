# 5427 불
import sys
from collections import deque

tc = int(input().strip())
for _ in range(tc):
  w, h = map(int, sys.stdin.readline().split())
  building = []
  person_q = deque([])
  fire_q = deque([])
  visited = [[0] * w for _ in range(h)]
  timer = 0
  flag = False  # 탈출 여부
  direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

  # 빌딩 정보 저장
  for i in range(h):
    temp = list(sys.stdin.readline().rstrip())
    building.append(temp)
    for j in range(w):
      if temp[j] == '@':
        person_q.append((i, j))
        visited[i][j] = 1
      elif temp[j] == '*':
        fire_q.append((i, j))

  # bfs 탐색 시작
  while person_q:

    # 불 확산
    for _ in range(len(fire_q)):
      fh, fw = fire_q.popleft()
      for dh, dw in direction:
        nfh, nfw = fh + dh, fw + dw

        if (0 <= nfw < w and 0 <= nfh < h and building[nfh][nfw] != '*'
            and building[nfh][nfw] != "#"):
          building[nfh][nfw] = "*"
          fire_q.append((nfh, nfw))

    # 상근이의 이동
    timer += 1  # 시간 경과
    for _ in range(len(person_q)):
      ph, pw = person_q.popleft()
      for dh, dw in direction:
        nph, npw = ph + dh, pw + dw

        if (0 <= npw < w and 0 <= nph < h):
          if visited[nph][npw] == 0 and building[nph][npw] == ".":
            visited[nph][npw] = 1
            person_q.append((nph, npw))
        else:
          flag = True
          break
      if flag:
        person_q = []
        break

  if flag:
    print(timer)
  else:
    print("IMPOSSIBLE")
