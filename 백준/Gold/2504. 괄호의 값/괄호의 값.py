string = list(input().strip())

stack = []
cnt = 1
total = 0

for i in range(len(string)):
  if string[i] == "(":
    cnt = cnt * 2
    stack.append(string[i])

  elif string[i] == "[":
    cnt = cnt * 3
    stack.append(string[i])

  elif string[i] == ")":
    if not stack or stack[-1] != "(":
      total = 0
      break
    if string[i - 1] == "(":
      total = total + cnt
    cnt = cnt // 2
    stack.pop()

  elif string[i] == "]":
    if not stack or stack[-1] != "[":
      total = 0
      break
    if string[i - 1] == "[":
      total = total + cnt
    cnt = cnt // 3
    stack.pop()

if stack:
  print(0)
else:
  print(total)