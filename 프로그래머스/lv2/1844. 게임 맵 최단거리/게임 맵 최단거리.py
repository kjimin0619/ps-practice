from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    def bfs() :
        q = deque([(0,0,0)])
        visited = [[False for _ in range(m)] for _ in range(n)]
        while q :
            cx, cy, cnt = q.popleft()
            print(cx, cy, cnt)
            visited[cx][cy] = True
            if cx == n-1 and cy == m-1 :
                return cnt + 1
            
            for dx, dy in ([(0,1),(1,0),(-1,0),(0,-1)]) :
                nx = cx + dx
                ny = cy + dy
                
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] == 1 :
                    visited[nx][ny] = True
                    q.append((nx,ny,cnt+1))
        
        
        return -1
    res = bfs()
    return res