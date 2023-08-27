from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = []
    
    for i in range(n):
        maps[i] = list(maps[i])
    
    def bfs(x,y) :
        q = deque()
        q.append((x,y))
        temp = 0
        while q :
            cx, cy = q.popleft()
            visited[cx][cy] = True
            if maps[cx][cy] != "X" :
                temp += int(maps[cx][cy])
                for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = cx+i, cy+j
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X" :
                        visited[nx][ny] = True
                        q.append((nx,ny))
        answer.append(temp)
        
    for i in range(n):
        for j in range(m):
            if not visited[i][j] :
                bfs(i,j)
    answer = [i for i in answer if i != 0]
    if answer :
        answer = sorted(answer, key = lambda x : x)
        return answer
    else :
        return [-1]
    
