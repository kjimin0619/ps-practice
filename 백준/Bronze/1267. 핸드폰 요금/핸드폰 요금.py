import sys

n = int(input())
total = list(map(int, sys.stdin.readline().split()))
# y
y = 0
for i in range(n):
  y += (total[i] // 30 + 1) * 10
# m
m = 0
for i in range(n):
  m += (total[i] // 60 + 1) * 15

# 비용 계산
if y < m:
  print('Y', y)
elif y == m:
  print('Y M', y)
else:
  print('M', m)
