# 9466 텀 프로젝트
import sys
sys.setrecursionlimit(123456789)
t = int(sys.stdin.readline().strip())

# dfs
def dfs(x):
  global result
  visited[x] = 1  # 방문 처리
  cycle.append(x)  # 팀 후보군으로 넣기
  next = selection[x]

  if not visited[next]:
    dfs(next)  # 계속 탐색
  else:
    # 깊이 우선 탐색 끝
    if next in cycle:  # cycle이 만들어졌다면
      result += cycle[cycle.index(next):]  # cycle의 시작점부터 끝까지만 추출

for _ in range(t):
  n = int(sys.stdin.readline().strip())  # 학생 수
  visited = [0] * (n + 1)  # 팀 결성 여부
  selection = [0] + list(map(int, sys.stdin.readline().split()))  # 선택 결과
  result = []  # 결성된 팀

  # 팀 탐색하기
  for start in range(1, n + 1):
    # 아직 방문 안한 곳이라면
    if not visited[start]:
      cycle = []
      dfs(start)

  print(n - len(result))
