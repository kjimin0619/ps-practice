temp = input().strip()
stack = []
cnt = 0

for idx in range(len(temp)):
  if temp[idx] == "(":
    stack.append(temp[idx])
  else:
    stack.pop()
    if temp[idx - 1] == "(":  # 레이저
      cnt += len(stack)
    else:
      cnt += 1
print(cnt)
