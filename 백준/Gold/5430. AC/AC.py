import sys
from collections import deque

t = int(sys.stdin.readline().strip())  # 테스트케이스 개수
for _ in range(t):
  p = sys.stdin.readline().strip()  # 함수
  n = int(sys.stdin.readline().strip())  # 배열 원소의 개수

  nums = eval(sys.stdin.readline().strip())
  d = deque(nums)  # 배열

  isReverse = False  # popleft
  error = False

  for op in p:
    if op == "R":
      isReverse = not isReverse
    elif op == "D" and d:
      d.pop() if isReverse else d.popleft()
    else:
      error = True
      break

  # 결과 출력
  if error:
    print("error")
  else:
    # reverse에 맞춰서 배열 원소 출력
    if isReverse:
      print("[" + ",".join(map(str, list(reversed(d)))) + "]")
    else:
      print("[" + ",".join(map(str, list(d))) + "]")
