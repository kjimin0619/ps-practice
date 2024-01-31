import sys

numbers = []
for _ in range(9):
  n = int(sys.stdin.readline().strip())
  numbers.append(n)

maxNum = max(numbers)
maxIdx = numbers.index(maxNum)

print(maxNum)
print(maxIdx + 1)