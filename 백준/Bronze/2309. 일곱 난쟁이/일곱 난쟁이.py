import sys
ppls = []
for _ in range(9):
  n = int(sys.stdin.readline().strip())
  ppls.append(n)

excepPpl = []
for i in range(9):
  for j in range(9):
    if i != j:
      if sum(ppls) - ppls[i] - ppls[j] == 100:
        excepPpl.append(i)
        excepPpl.append(j)
        break
  if len(excepPpl) == 2:
    break

newPpl = [ppls[i] for i in range(9) if i not in excepPpl]
newPpl.sort()
for p in newPpl:
  print(p)
