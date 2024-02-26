import sys
from collections import deque

n = int(sys.stdin.readline().strip())
d = deque([i for i in range(1, n + 1)])
while len(d) > 1:
  top = d.popleft()
  nextTop = d.popleft()
  d.append(nextTop)

print(d.pop())