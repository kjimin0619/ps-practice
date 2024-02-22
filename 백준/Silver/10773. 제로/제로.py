from sys import stdin as s

stack = []

k = int(s.readline().strip())
for _ in range(k):
  temp = int(s.readline().strip())
  if temp == 0:
    stack.pop(-1)
  else:
    stack.append(temp)

print(sum(stack))
