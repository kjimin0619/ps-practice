import sys

input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]  # 계단
result = [0] * n
    
if n <= 2:
  print(sum(s))

else:
  # 계단이 3개 이상일 때 구현
  result[0] = s[0]
  result[1] = s[0] + s[1]
  result[2] = max(s[0] + s[2], s[1] + s[2])

  for i in range(3, n):
    result[i] = result[i] + max(result[i - 3] + s[i - 1] + s[i],
                                result[i - 2] + s[i])

  print(result[n - 1])
