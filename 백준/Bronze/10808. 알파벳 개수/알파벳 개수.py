import sys

s = sys.stdin.readline().strip()

alpha = [0] * 26
for a in s:
  idx = ord(a) - 97
  alpha[idx] += 1

print(*alpha)

