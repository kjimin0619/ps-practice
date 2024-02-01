import math

n = int(input())
nums = [0] * 10

strN = str(n)
for i in strN:
  nums[int(i)] += 1

# 6,9 처리
nums[9] = math.ceil((nums[6] + nums[9]) / 2)
nums[6] = 0

print(max(nums))
