# 5014 스타트링크
from collections import deque

f, s, g, u, d = map(int, input().split())
deq = deque([s])
visited = [0] * (f + 1)
visited[s] = 1
flag = 0
cnt = 0

while deq:
  for _ in range(len(deq)):
    cur = deq.popleft()
    if cur == g:
      deq = []
      flag = 1
      break

    newU = cur + u
    newD = cur - d

    if 0 < newU <= f and visited[newU] == 0:
      visited[newU] = 1
      deq.append(newU)

    if 0 < newD <= f and visited[newD] == 0:
      visited[newD] = 1
      deq.append(newD)
  cnt += 1

if flag:
  print(cnt - 1)
else:
  print("use the stairs")
