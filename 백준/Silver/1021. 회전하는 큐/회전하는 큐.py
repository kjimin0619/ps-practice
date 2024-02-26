import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
target_pos = list(map(int, sys.stdin.readline().split()))
d = deque([i + 1 for i in range(n)])
cnt = 0  # 덱 자리 교환 연산 횟수

for i in range(m):
  if d[0] != target_pos[i]:
    # 자리 교환 연산 수행
    pos = d.index(target_pos[i])
    if pos <= (len(d) // 2):
      # 왼쪽으로 이동
      while d[0] != target_pos[i]:
        d.append(d.popleft())
        cnt += 1
    else:
      while d[0] != target_pos[i]:
        # 오른쪽으로 이동
        d.appendleft(d.pop())
        cnt += 1

  d.popleft()

print(cnt)
