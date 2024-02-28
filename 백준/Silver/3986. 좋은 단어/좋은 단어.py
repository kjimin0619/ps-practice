from re import L
import sys

n = int(sys.stdin.readline().strip())  # 단어의 개수

cnt = 0
for _ in range(n):
  temp = sys.stdin.readline().strip()

  if (len(temp) % 2 == 0):
    # 선이 교차하는지 검사
    stack = []
    for w in temp:
      if stack:
        if stack[-1] == w:
          stack.pop(-1)
        else:
          stack.append(w)
      else:
        stack.append(w)

    if not stack:
      cnt += 1

print(cnt)
