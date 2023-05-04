# 1260
# DFS, BFS 간단 구현
from sys import stdin as s
from collections import deque

#s = open("input.txt", "rt")
N, M, V = map(int,s.readline().split())

# 그래프 초기화
# True False로 구현
graph = [[False] * (N + 1) for _ in range(N + 1)]

# 간선의 정보 입력받기
for _ in range(M):
  n1, n2 = map(int,s.readline().split())
  graph[n1][n2] = True
  graph[n2][n1] = True

visited_b = [False] * (N + 1)  # bfs 방문 기록
visited_d = [False] * (N + 1)  # dfs 방문 기록

def bfs(V):
  # deque 사용
  q = deque([V])  # pop에서 시간복잡도가 낮은 deque 사용
  visited_b[V] = True # 시작 노드 방문 처리

  while (q): 
    now = q.popleft() # 가장 먼저 들어간 노드 빼내기
    visited_b[now] = True
    print(now, end=' ')
    for i in range(1, N + 1):
      connection = graph[now]
      if ((visited_b[i] == False) and (connection[i] == True)):
        visited_b[i] = True  # 방문 표시
        q.append(i)



def dfs(V):
  # 재귀
  visited_d[V] = True
  print(V, end = ' ')
  for i in range(N+1):
    if (visited_d[i] == False and graph[V][i] == True):
      dfs(i)
  return

dfs(V)
print()
bfs(V)

