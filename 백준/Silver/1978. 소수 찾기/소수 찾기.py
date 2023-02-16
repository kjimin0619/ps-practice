import sys
import math
n = int(input())
nums = list(map(int,sys.stdin.readline().split()))

def isPrime(n):
    if n == 1 : return False
    for i in range(2,n//2 +1) :
        if (n%i == 0) : return False
    return True
        
print(len([i for i in nums if isPrime(i)]))