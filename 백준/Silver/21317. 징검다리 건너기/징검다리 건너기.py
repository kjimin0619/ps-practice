from sys import stdin as s
from copy import deepcopy

n = int(s.readline()) # 돌의 개수
small = []
large = []
for _ in range(n-1):
    m, b = map(int, s.readline().split())
    small.append(m)
    large.append(b)

k = int(s.readline()) # 제일 큰 점프

if n == 1 :
    print(0)
elif n == 2 :
    print(small[0])
elif n == 3 :
    print(min(sum(small), large[0]))
else :
    answer = []
    # 슈퍼 점프 고려 X
    dp=[0]*n
    dp[1] = small[0]

    for i in range(2,n):
        dp[i] = min(dp[i-1] + small[i-1], # 직전 돌에서 건너오기
                    dp[i-2] + large[i-2] # 2칸 전 돌에서 건너오기
        )
    answer.append(dp[n-1])

    # 슈퍼 점프 고려 O
    for m in range(n-3):
        temp = deepcopy(dp)
        temp[m+3] = dp[m] + k

        for j in range(m+4, n):
            temp[j] = min(temp[j-1] + small[j-1],
                          temp[j-2] + large[j-2])
        answer.append(temp[n-1])

    print(min(answer))
