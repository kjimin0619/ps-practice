# 13549 숨바꼭질
from collections import deque

n, k = map(int, input().split())
d = deque([n])
end = n if n > k else k
dist = [-1] * (end * 2 + 1)
dist[n] = 0

while d:
  cur = d.popleft()
  if cur == k:
    print(dist[cur])
    break

  for i in range(3):
    if i == 0:
      next = cur + 1
    elif i == 1:
      next = cur - 1
    else:
      next = cur * 2

    if (0 <= next <= end * 2):
      # 첫 방문하는 위치라면
      if dist[next] == -1:
        d.append(next)
        if i == 2:
          dist[next] = dist[cur]  # 순간이동
        else:
          dist[next] = dist[cur] + 1  # 옆으로 이동
      # 첫 방문은 아니지만, 순간이동이 더 빠르다면
      elif i == 2 and dist[next] > dist[cur]:
        dist[next] = dist[cur]
      elif i != 2 and dist[next] > dist[cur] + 1:
        dist[next] = dist[cur] + 1
