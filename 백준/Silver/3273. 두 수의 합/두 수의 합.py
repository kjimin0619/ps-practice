import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
x = int(input())

nums.sort()

left = 0
right = n - 1
cnt = 0

while left < right:
  if nums[left] + nums[right] > x:
    right -= 1
  elif nums[left] + nums[right] < x:
    left += 1
  else:
    cnt += 1
    left += 1

print(cnt)
