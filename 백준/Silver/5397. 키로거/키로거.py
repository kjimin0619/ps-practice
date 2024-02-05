tc = int(input())
for _ in range(tc):
  l_pwd = []
  r_pwd = []

  t = input().strip()

  for a in t:
    if a == "-":
      if l_pwd:
        l_pwd.pop()
    elif a == "<":
      if l_pwd:
        r_pwd.append(l_pwd.pop())
    elif a == ">":
      if r_pwd:
        l_pwd.append(r_pwd.pop())
    else:
      l_pwd.append(a)

  print(''.join(l_pwd), ''.join(r_pwd[::-1]), sep="")