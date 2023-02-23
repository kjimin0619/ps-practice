a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

# n0보다 크거나 같은 모든 n에 대하여, n >= a0 // (c-a1) 성립
for n in range(n0, 101) :
    if (a1*n+a0 > c*n): 
        print(0)
        break
else :
    print(1)
