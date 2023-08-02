from sys import stdin as s
from collections import deque

m, n = map(int,s.readline().split())
tomato = []
start = []

for i in range(n):
    temp = list(map(int,s.readline().split()))
    for j in range(m) :
        if temp[j] == 1 :
            start.append((i,j))
        
    tomato.append(temp)

def bfs():
    q = deque(start)
    
    while q :
        curr_x, curr_y = q.popleft()
        day = tomato[curr_x][curr_y]
        
        for (i,j) in [(-1,0),(1,0),(0,1),(0,-1)] :
            _x = curr_x + i
            _y = curr_y + j

            if (0 <= _x < n and 
                0 <= _y < m and 
                tomato[_x][_y] == 0 ) :
                
                q.append((_x, _y))
                tomato[_x][_y] = day + 1
bfs()

if all(0 not in L for L in tomato) :
    print(max(map(max, tomato)) - 1)
else :
    print(-1)