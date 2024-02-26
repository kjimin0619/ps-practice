import sys
from collections import deque

n = int(sys.stdin.readline().strip())
d = deque()
for _ in range(n):
  op = sys.stdin.readline().split()
  if op[0] == "push":
    d.append(int(op[1]))
  elif op[0] == "pop":
    print(d.popleft() if d else "-1")
  elif op[0] == "size":
    print(len(d))
  elif op[0] == "empty":
    print("0" if d else "1")
  elif op[0] == "front":
    print(d[0] if d else "-1")
  else:
    print(d[-1] if d else "-1")
