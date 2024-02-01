import math

total, k = map(int, input().split())
zeros = [0, 0, 0, 0, 0, 0]
ones = [0, 0, 0, 0, 0, 0]

for _ in range(total):
  type, nums = map(int, input().split())
  if type:
    ones[nums - 1] += 1
  else:
    zeros[nums - 1] += 1

newZero = [math.ceil(i / k) for i in zeros if i > 0]
newOne = [math.ceil(i / k) for i in ones if i > 0]

print(sum(newZero) + sum(newOne))
