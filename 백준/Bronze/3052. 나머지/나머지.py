import sys
nums = set()
for _ in range(10) :
    i = int(sys.stdin.readline())
    i %= 42
    nums.add(i)

print(len(nums))