import sys
numbers = []
for _ in range(9):
    numbers.append(int(sys.stdin.readline()))

m = max(numbers)
print(m)
print(numbers.index(m)+1)