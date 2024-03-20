# 9466 텀 프로젝트
import sys

sys.setrecursionlimit(123456789)
t = int(sys.stdin.readline().strip())  # 테스트케이스 개수


def dfs(starter):
  visited[starter] = 1  # 현재 타자 방문 기록
  group.append(starter)
  next = selection[starter]  # 현재 타자가 지목한 상대
  global result

  if not visited[next]:
    dfs(next)
  elif next in group:
    result += len(group[group.index(next):])


for _ in range(t):
  #### round start ####
  n = int(sys.stdin.readline().strip())  # 사람 수
  visited = [0] + [0] * n  # 방문여부
  selection = [0] + list(map(int, sys.stdin.readline().split()))  # 작대기

  result = 0  # 팀 결성에 성공한 학생들

  for ppl in range(1, n + 1):
    if not visited[ppl]:
      group = []  # 방문자 담을 임시 리스트
      dfs(ppl)

  print(n - result)
  #### round fin. ####
