from sys import stdin as s
n,m = map(int, s.readline().split())
sx, sy, d = map(int, s.readline().split())
direction = [(-1,0),(0,1),(1,0),(0,-1)]
board = []

for _ in range(n):
    board.append(list(map(int, s.readline().split())))

def rotateD(d):
    if d == 0 :
        return 3
    else :
        return d-1

def backD(d):
    if d == 0 :
        return 2
    elif d == 1 :
        return 3
    elif d == 2 :
        return 0
    else :
        return 1
    
def check(cx, cy) :
    for i,j in direction :
        if 0 <= cx+i < n and 0 <= cy+j < m and board[cx+i][cy+j] == 0 :
            return True
    return False
    
cnt = 0
x = sx 
y = sy

while cnt <= n * m :
    if board[x][y] == 0 :
        board[x][y] = 2  # 청소
        cnt += 1
    
    # 빈칸이 없는 경우
    if not check(x,y):
        # 후진 가능하면
        bx, by = direction[backD(d)]
        if 0 <= x+bx < n and 0 <= y+by < m and board[x+bx][y+by] != 1 :
            x = x + bx
            y = y + by
        else :
            break
        
    # 빈칸이 있는 경우
    else :
        cx, cy = x , y
        while True:
            d = rotateD(d)
            cx = x + direction[d][0]
            cy = y + direction[d][1]
            if 0 <= cx < n and 0 <= cy < m and board[cx][cy] == 0 :
                break
    
        x = cx
        y = cy
        
print(cnt)