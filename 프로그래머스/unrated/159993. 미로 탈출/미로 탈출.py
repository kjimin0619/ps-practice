from collections import deque
def bfs(s, e, maps):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    flag = False
    for i in range(n):
        for j in range(m):
            if maps[i][j] == s:
                q.append((i, j, 0)) # start node queue에 추가
                visited[i][j] = True # 방문 처리
                flag = True
                break
        if flag:
            break

    while q:
        y, x, cost = q.popleft()
        if maps[y][x] == e:
            return cost
        for i in range(4): # 상, 하, 좌, 우 4가지 방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'X': # 갈수 있는 경로에 있는 경우
                if not visited[ny][nx]:
                    q.append((ny, nx, cost+1))
                    visited[ny][nx] = True
    return -1
def solution(maps):
    path1 = bfs('S', 'L', maps) # 시작점부터 레버까지 거리
    path2 = bfs('L', 'E', maps) # 레버부터 출구까지 거리
    if path1 != -1 and path2 != -1:
        return path1 + path2
    return -1