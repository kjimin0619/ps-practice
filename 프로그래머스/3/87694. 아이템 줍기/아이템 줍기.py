from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 맵 2배로 확장시키기
    board = [[0] * 110 for _ in range(110)] # 갈 수 있는 길 표시
    new_rectangle = []
    
    for x1, y1, x2, y2 in rectangle :
        x1, y1, x2, y2 =  x1*2, y1*2, x2*2, y2*2 
        new_rectangle.append((x1, y1, x2, y2))
        # 보드판에 칠하기 (갈 수 있는길 표시)
        for x in range(x1, x2+1) :
            for y in range(y1, y2+1) :
                 board[x][y] = 1
                    
    # 테두리 내부는 0으로 표시하기
    for i1,j1, i2,j2 in new_rectangle :
        for i in range(i1+1, i2) :
            for j in range(j1+1, j2) :
                board[i][j] = 0
                
    # bfs 준비            
    direction = [(-1,0),(1,0),(0,1),(0,-1)]
    q = deque([(characterX*2, characterY*2, 0)]) # 시작 x, 시작 y, 이동횟수
    visited = set()
    visited.add((characterX*2, characterY*2)) # 방문 기록
    
    # bfs 탐색 시작
    while q :
        curX, curY, curL = q.popleft()
        
        for dx, dy in direction :
            newX, newY = curX+dx, curY+dy
            # 도착 했으면,
            if newX == itemX*2 and newY == itemY*2 :
                return (curL+1) // 2
                
            # 방문 안 한 갈 수 있는 테두리라면,
            if board[newX][newY] == 1 and (newX, newY) not in visited :
                visited.add((newX, newY)) # 방문 처리
                q.append((newX, newY, curL +1))
    

    
    
    return answer