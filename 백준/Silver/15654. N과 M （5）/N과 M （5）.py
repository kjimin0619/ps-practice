from sys import stdin as s
from itertools import permutations

n, m = map(int, s.readline().split())
numbers = list(map(int,s.readline().split()))
numbers.sort()

for i in list(permutations(numbers, m)) :
    print(*i, end=" ")
    print()