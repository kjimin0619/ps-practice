# 1697
from collections import deque

n, k = map(int, input().split())  # n 수빈, k 동생
q = deque([n])
graph = [0] * 1000001
graph[n] = 1

while q:
  pos = q.popleft()
  if pos == k:
    print(graph[k] - 1)
    break

  for newPos in (pos + 1, pos - 1, pos * 2):
    if 0 <= newPos <= 100000:
      if graph[newPos] == 0 or graph[newPos] > graph[pos] + 1:
        graph[newPos] = graph[pos] + 1
        q.append(newPos)
