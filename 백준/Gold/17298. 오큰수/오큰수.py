# 17298 오큰수
import sys as s

n = int(s.stdin.readline().strip())
nums = list(map(int, s.stdin.readline().split()))
stack = []
nge = [-1] * n

for i in range(n):
  while stack and nums[stack[-1]] < nums[i]:
    nge[stack.pop()] = nums[i]
  stack.append(i)

print(*nge)
