def d(n) :
    a = n // 10000
    b = (n % 10000) // 1000
    b_ = (n % 10000) % 1000
    c = b_ // 100
    c_ = b_ % 100
    d = c_ // 10
    e = c_ % 10
    return n + a + b + c + d + e

allNum = [i for i in range(1,10001)]

for i in range(1,10001) :
    delNum = d(i)
    if delNum in allNum : allNum.remove(delNum)
  
for selfNum in allNum :
    print(selfNum)