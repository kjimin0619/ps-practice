import sys
num, x =  map(int, sys.stdin.readline().split(" "))
numList = list(map(int, sys.stdin.readline().split(" ")))

for i in numList :
    if i < x : print(i, end = " ")