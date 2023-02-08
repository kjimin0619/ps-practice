import sys

while True :
    a,b = map(int, sys.stdin.readline().split(" "))
    if not(a or b) : break
    print(a+b)
