import math
n = int(input())

# DP : python3으로 채점하면 시간초과
# dp = [0]*(n+1)
# dp[1] = 1
# for i in range(2,n+1):
#     quo = math.floor(math.sqrt(i))
#     remain = i - quo*quo
#     min_value = dp[remain]

#     for k in range(1, quo+1):
#         min_value = min(min_value, dp[i - k*k])

#     dp[i] = min_value + 1

#print(dp[-1])

## python3로 시간초과 안나는 코드 (BF)
from itertools import combinations_with_replacement

square1 = [i*i for i in range(int(math.sqrt(n))+1)] # 모든 제곱수(n 이하의)
temp = list(combinations_with_replacement(square1,2))
square2 = [sum(k) for k in combinations_with_replacement(square1,2)] # 가능한 모든 제곱수 2개의 합

def solve_bf(n):
    if n in square1:
        return 1
    elif n in square2 :
        return 2
    else :
        for square in square1:
            if n - square in square2 :
                return 3
    return 4

print(solve_bf(n))
