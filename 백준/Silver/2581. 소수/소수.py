m = int(input())
n = int(input())

def isPrime(n):
    if n == 1 : return False
    for i in range(2,n//2 +1) :
        if (n%i == 0) : return False
    return True
    
result = [i for i in range(m,n+1) if isPrime(i)]

if len(result) >= 1 :
    print(sum(result))
    print(min(result))
else :
    print(-1)