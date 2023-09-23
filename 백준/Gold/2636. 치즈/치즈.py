from sys import stdin as s
from collections import deque

n,m = map(int, s.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, s.readline().split())))

counts = []
def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque([])
    q.append((0,0))
    cnt = 0
    
    while q :
        x,y = q.popleft()
        for dx, dy in [(-1,0),(0,1),(0,-1),(1,0)]:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                if board[nx][ny] == 0 :
                    visited[nx][ny] = True
                    q.append((nx,ny))
                elif board[nx][ny] == 1 :
                    visited[nx][ny] = True
                    cnt += 1
                    board[nx][ny] = 0

    if cnt > 0 :
        counts.append(cnt)
    return cnt

while True :
    ans = bfs()
    if ans == 0 :
        break
    
print(len(counts), counts[-1])