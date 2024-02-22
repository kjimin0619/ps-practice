from sys import stdin as s

stack = []
op = []
n = int(s.readline().strip())

i = 1
flag = 0

for _ in range(n):
  temp = int(s.readline().strip())
  
  while i <= temp:
    stack.append(i)
    op.append("+")  # push
    i += 1

  if stack[-1] == temp:
    stack.pop(-1)
    op.append("-")  # pop

  else:
    print("NO")
    flag = 1
    break

if flag == 0:
  for o in op:
    print(o)
