# 2573 빙산
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time = 0  # 시간의 경과
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 이동 방향


# 주변 탐색
def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = 1

  while q:
    cx, cy = q.popleft()  # 현 위치
    for dx, dy in direction:
      nx, ny = cx + dx, cy + dy
      if (0 <= nx < n and 0 <= ny < m):
        if graph[nx][ny] == 0:  # 주변이 바다
          visited[cx][cy] += 1  # 현 위치 방문 정보에 바다 개수 저장

        if visited[nx][ny] == 0 and graph[nx][ny] != 0:  # 주변이 빙하
          q.append((nx, ny))
          visited[nx][ny] = 1


while True:
  count = 0  # 생성된 빙하 덩어리 수
  visited = [[0] * m for _ in range(n)]  # 방문 여부
  # 빙하 덩어리 탐색 후 카운팅
  for i in range(n):
    for j in range(m):
      if visited[i][j] == 0 and graph[i][j] > 0:
        bfs(i, j)
        count += 1  # bfs로 찾은 빙하 덩어리 한 개

  # 빙하 녹이기
  for i in range(n):
    for j in range(m):
      if visited[i][j] != 0:
        graph[i][j] -= (visited[i][j] - 1)
        if graph[i][j] < 0:
          graph[i][j] = 0

  # 빙하 덩어리 검사
  if count >= 2:
    print(time)
    break

  if count == 0:
    print(0)
    break

  time += 1  # 1년 흐름