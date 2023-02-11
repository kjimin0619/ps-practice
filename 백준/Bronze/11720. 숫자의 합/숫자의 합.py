import sys

n = int(sys.stdin.readline())
nums = sys.stdin.readline().strip()
sum = 0
for num in nums :
    sum += int(num)
print(sum)