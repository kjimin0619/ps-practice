from sys import stdin as s
from collections import deque

n,m = map(int,s.readline().split())
goal = (0,0)
graph = []
distance = [[-1 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

# 그래프 정보 입력받기
for i in range(n):
    numbers = list(map(int, s.readline().split()))
    graph.append(numbers)

    for j in range(m) :
        if numbers[j] == 2 :
            goal = (i,j)

# goal에서 시작하여 모든 지점까지의 경로 구하기
def bfs(x,y):
    direct = [(0,1),(0,-1),(1,0),(-1,0)]
    q = deque()
    q.append((x,y))
    visited[x][y]= 1
    distance[x][y] = 0
    
    while q:
        _x, _y = q.popleft()

        for d_x, d_y in direct :
            new_x = d_x + _x
            new_y = d_y + _y
            
            if (0<= new_x <n 
                and 0<= new_y < m 
                and visited[new_x][new_y] == 0) :

                visited[new_x][new_y] = 1
                if graph[new_x][new_y] == 0 :
                    distance[new_x][new_y] = 0
                else :
                    distance[new_x][new_y] = distance[_x][_y] + 1
                    q.append((new_x, new_y))

bfs(goal[0],goal[1])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end = " ")
        else:
            print(distance[i][j], end = " ")
    print()


