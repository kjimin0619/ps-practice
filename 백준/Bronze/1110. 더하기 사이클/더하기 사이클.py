import sys

n = int(sys.stdin.readline())
count = 0
newNum = n

while True :
    a = newNum // 10
    b = newNum % 10
    c = (a+b) % 10
    newNum = 10*b + c
    
    count += 1
    if (n == newNum) :
        break
    
print(count)