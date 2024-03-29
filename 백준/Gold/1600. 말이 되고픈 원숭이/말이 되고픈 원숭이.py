# 1600 말이 되고픈 원숭이
from collections import deque

k = int(input().strip())
w, h = map(int, input().split())
horse_mv = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2),
            (2, 1)]  # 말이 움직이는 방식
monkey_mv = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 원숭이가 움직이는 방식

board = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]  # 이동횟수 행, 열
d = deque([(0, 0, 0)])
flag = 0  # 도착여부
visited[0][0][0] = 1  # 시작 지점
while d:
  cnt, ch, cw = d.popleft()

  # 도착
  if (ch == h - 1 and cw == w - 1):
    print(visited[cnt][ch][cw] - 1)  # 시작지점 이동횟수 제외
    flag = 1
    break

  # 원숭이처럼 이동
  for i, j in monkey_mv:
    nh, nw = ch + i, cw + j
    if (0 <= nh < h and 0 <= nw < w and board[nh][nw] != 1
        and not visited[cnt][nh][nw]):
      visited[cnt][nh][nw] = visited[cnt][ch][cw] + 1
      d.append((cnt, nh, nw))

  # 말처럼 이동
  if cnt < k:
    for i, j in horse_mv:
      hh, hw = ch + i, cw + j
      if (0 <= hh < h and 0 <= hw < w and board[hh][hw] != 1):
        # 말처럼 이동
        if not visited[cnt + 1][hh][hw]:
          visited[cnt + 1][hh][hw] = visited[cnt][ch][cw] + 1
          d.append((cnt + 1, hh, hw))

if not flag:
  print(-1)
