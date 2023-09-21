from sys import stdin as s
from collections import deque
from itertools import combinations
import copy

n,m = map(int,s.readline().split())
board = []
bomb = []
for i in range(n):
    board.append(list(map(int, s.readline().split())))
    for j in range(m):
        if board[i][j] == 2 :
            bomb.append((i,j))

# 빈 공간 계산
def count_zero(brd):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if brd[i][j] == 0 :
                cnt += 1
    return cnt

# 바이러스 전파
def spread(brd, walls):
    after_spread = copy.deepcopy(brd)
    for i,j in walls :
        after_spread[i][j] = 1 # 벽 세우기
    
    for x,y in bomb :
        q = deque([(x,y)])
        while q :
            cx,cy = q.popleft()
            for (dx, dy) in [(-1,0),(0,1),(1,0),(0,-1)]:
                nx ,ny = cx+dx , cy+dy    
                if (0 <= nx < n and 0 <= ny < m and 
                    after_spread[nx][ny] == 0 and
                    after_spread[nx][ny] != 2) :
                    
                    after_spread[nx][ny] = 2
                    q.appendleft((nx,ny))            
    return after_spread

walls = []
cnt_max = 0
# 세울 수 있는 모든 벽 구하기
for i in range(n):
    for j in range(m) :
        if board[i][j] == 0:
            walls.append((i,j))

for wlls in list(combinations(walls, 3)):
    after_spread = spread(board, wlls)
    cnt_max = max(count_zero(after_spread), cnt_max)
print(cnt_max)