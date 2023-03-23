# 투에모스 수열의 점화식 활용
def solve(idx: int):
  if idx == 0:
    return 0
  elif idx == 1:
    return 1
  elif idx % 2 == 0:
    return solve(idx // 2)
  else:
    return 1 - solve(idx // 2)


k = int(input())
print(solve(k-1))
