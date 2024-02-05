import sys

left = list(input().strip())
tc = int(input())

right = []

for _ in range(tc):
  op = sys.stdin.readline().split()
  if op[0] == 'L' and left:  # 왼쪽 이동
    right.append(left.pop())

  elif op[0] == 'D' and right:  # 오른쪽 이
    left.append(right.pop())

  elif op[0] == 'B' and left:  # 커서 왼쪽 문자 삭제
    left.pop()

  elif op[0] == 'P':
    left.append(op[1])

print(''.join(left), ''.join(right[::-1]), sep="")
