# 2630 색종이 만들기
import sys
input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]


def find_222_pooling(lst, n):
  if n == 1: return lst
  r, c = 0, 0  # 행 길이 슬라이스, 열
  result = []

  for _ in range(n // 2):
    line = []
    for _ in range(n // 2):
      two_by_two = [lst[r][c:c + 2], lst[r + 1][c:c + 2]]
      c += 2
      line.append(find_second(sum(two_by_two, [])))

    # 가로 방향 탐색 끝
    result.append(line)
    c = 0
    r += 2

  # 모든 방향 탐색 끝
  return find_222_pooling(result, n // 2)


def find_second(mtrx):
    mtrx.remove(max(mtrx))
    sec = max(mtrx)
    return sec


ans = find_222_pooling(nums, N)
print(ans[0][0])
