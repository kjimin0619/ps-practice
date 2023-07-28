n, m = map(int,input().split())

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

if n == m :
    print(1)
else :
    # 분모
    res = 1
    for i in range(m):
        res = res * n
        n = n - 1

    # 분자
    b = factorial(m)
    print(res//b)