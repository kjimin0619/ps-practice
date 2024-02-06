import sys

n, k = map(int, sys.stdin.readline().split())
answer = []
ppl = [i + 1 for i in range(n)]

idx = 0
for _ in range(n):
  idx += (k - 1)
  if idx >= len(ppl):
    idx = idx % len(ppl)

  target = ppl.pop(idx)
  answer.append(str(target))

print("<", ', '.join(answer), ">", sep="")
