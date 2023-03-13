# 2630 색종이 만들기
import sys

input = sys.stdin.readline

n = int(input())  # 종이 한 변의 길이
papers = [list(map(int, input().split())) for _ in range(n)]  # 색종이들

result = []


def cut(x, y, n):  # 행 출발점, 열 출발점, 길이
  color = papers[x][y]  # 첫 번째 색

  for i in range(x, x + n):
    for j in range(y, y + n):
      if color != papers[i][j]:
        cut(x, y, n // 2)  # 1사분면
        cut(x, y + n // 2, n // 2)  # 2사분면
        cut(x + n // 2, y, n // 2)  # 3사분면
        cut(x + n // 2, y + n // 2, n // 2)  # 4사분면
        return

  # divide 종료
  if color == 0: result.append(0)
  else: result.append(1)


cut(0, 0, n)
print(result.count(0), result.count(1), sep='\n')
