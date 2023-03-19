N = int(input())
PAPERS = [list(map(int, input().split())) for _ in range(N)]
CNT = [0, 0, 0]  # -1, 0, 1 카운트

# 종이 판별
def is_all_same(x, y, cnt):
  pivot = PAPERS[x][y]
  for i in range(cnt):
    for j in range(cnt):
      if pivot != PAPERS[x+i][y+j]:
        return False
  return True


# divide and conquer
def solve(x, y, n):
  if is_all_same(x, y, n) or n == 1:
    idx = PAPERS[x][y] + 1
    CNT[idx] += 1
    return

  else:
    newN = n // 3  # 나눠진 색종이의 길이
    # top
    solve(x, y, newN)
    solve(x, y + newN, newN)
    solve(x, y + newN + newN, newN)

    # middle
    solve(x + newN, y, newN)
    solve(x + newN, y + newN, newN)
    solve(x + newN, y + newN + newN, newN)

    #bottom
    solve(x + newN + newN, y, newN)
    solve(x + newN + newN, y + newN, newN)
    solve(x + newN + newN, y + newN + newN, newN)
    
    return


solve(0, 0, N)
print(CNT[0], CNT[1], CNT[2], sep='\n')
