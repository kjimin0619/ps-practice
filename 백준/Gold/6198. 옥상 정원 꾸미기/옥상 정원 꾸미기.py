# 6198
import sys as s

n = int(s.stdin.readline().strip())
height = [int(s.stdin.readline().strip()) for _ in range(n)]

stack = []
cnt = 0

for cur in height:
  while stack and stack[-1] <= cur:
    # 현 빌딩 옥상을 볼 수 없는 것들은 전부 제거
    stack.pop()

  cnt += len(stack)
  stack.append(cur)  # 현 빌딩 스택에 추가

print(cnt)
