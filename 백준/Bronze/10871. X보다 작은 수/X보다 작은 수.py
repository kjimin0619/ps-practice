import sys

n, x = map(int, sys.stdin.readline().split(" "))
myList = list(map(int, sys.stdin.readline().split(" ")))

for num in myList:
  if num < x: print(num, end=" ")
