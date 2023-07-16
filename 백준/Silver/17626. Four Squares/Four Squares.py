import math
n = int(input())

# n보다 작거나 같은 제곱수를 찾은 후
# "n-제곱수"를 인덱스로 가진 값에 1을 더해준다

dp = [0]*(n+1)
dp[1] = 1
for i in range(2,n+1):
    quo = math.floor(math.sqrt(i))
    remain = i - quo*quo
    min_value = dp[remain]

    for k in range(1, quo+1):
        min_value = min(min_value, dp[i - k*k])

    dp[i] = min_value + 1

print(dp[-1])
