import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
  stack = []
  flag = True
  sentence = sys.stdin.readline().strip()

  for w in sentence:
    if w == '(':
      stack.append(w)
    else:
      if stack:
        if stack[-1] == '(':
          stack.pop(-1)
        else:
          flag = False
          break
      else:
        flag = False
        break

  if not stack and flag:
    print("YES")
  else:
    print("NO")
