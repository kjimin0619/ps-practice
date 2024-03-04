from collections import deque

r, c = map(int, input().split())
maze = []

q_j = deque([])  # 지훈 이동 큐
q_f = deque([])  # 불 이동 큐
ans = 0  # 시간의 경과
flag = False  # 탈출 여부
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visited_j = [[0] * c for _ in range(r)]  # 지훈 방문 처리
visited_f = [[0] * c for _ in range(r)]  # 불 방문 처리

# 미로 정보
for i in range(r):
  maze.append(list(input().rstrip()))
  for j in range(c):
    if maze[i][j] == "J":
      q_j.append((i, j))
      visited_j[i][j] = 1
    elif maze[i][j] == "F":
      q_f.append((i, j))
      visited_f[i][j] = 1

while q_j:
  # 불 확산
  for _ in range(len(q_f)):
    fx, fy = q_f.popleft()
    for dx, dy in directions:
      nfx, nfy = fx + dx, fy + dy
      if 0 <= nfx < r and 0 <= nfy < c and visited_f[nfx][
          nfy] == 0 and maze[nfx][nfy] != "#":
        # 불 번지는 과정
        maze[nfx][nfy] = "F"
        q_f.append((nfx, nfy))
        visited_f[nfx][nfy] = 1

  # 지훈이 이동
  for _ in range(len(q_j)):
    cx, cy = q_j.popleft()
    for dx, dy in directions:
      nx, ny = cx + dx, cy + dy
      if 0 <= nx < r and 0 <= ny < c:
        if maze[nx][ny] == "." and visited_j[nx][ny] == 0:
          visited_j[nx][ny] = 1
          q_j.append((nx, ny))
      else:
        # 탈출 성공
        flag = True
        q_j = []
        break
    if flag:
      break

  ans += 1

# 결과 출력
if flag:
  print(ans)
else:
  print("IMPOSSIBLE")
