# 13913 숨바꼭질4
from collections import deque

n, k = map(int, input().split())
visited = [[0, -1] for _ in range(100001)]
record = {}
visited[n][0] = 1
d = deque([n])

while d:
  cur = d.popleft()
  if cur == k:
    print(visited[cur][0] - 1)
    break

  for i in range(3):
    if i == 0:
      next = cur + 1
    elif i == 1:
      next = cur - 1
    else:
      next = cur * 2

    if 0 <= next < 100001 and visited[next][0] == 0:
      visited[next][0] = visited[cur][0] + 1
      visited[next][1] = cur
      d.append(next)

c = k
revAns = [k]
while True:
  c = visited[c][1]
  if c == -1:
    break
  else:
    revAns.append(c)

print(*revAns[::-1])
