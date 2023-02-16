n = (123456*2+1)
primeList = [1] * (n)

for i in range(1,n):
    if i == 1 :
        continue
    for j in range(2, int(i**0.5)+1) :
        if i%j == 0 : 
            primeList[i] = 0
            break

while True:
    n = int(input())
    if n == 0 : 
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        cnt += primeList[i]
    print(cnt)
