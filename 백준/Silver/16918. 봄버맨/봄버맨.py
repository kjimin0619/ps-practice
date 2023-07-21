from collections import deque
from sys import stdin as s

r,c,n = map(int,s.readline().strip().split())

ground = []
for i in range(r):
    ground.append(list(s.readline().strip()))

bomb= deque()
dir = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]

# 폭탄 터트리는 함수
def explode(bomb, grnd):
    while bomb :
        curr_x, curr_y = bomb.popleft()
        for (x,y) in dir :
            if -1 < (curr_x + x) < r and -1 < (curr_y+ y) < c :
                grnd[curr_x+x][curr_y+y] = '.'

def simulate(t):
    global bomb, ground # 함수 밖에 선언된 변수 가리킴

    if t == 1 :
        for i in range(r):
            for j in range(c):
                if ground[i][j] == 'O' :
                    bomb.append((i,j))

    # 폭탄터트리기
    elif t%2 == 1 :
        # 3초가 지난 폭탄 터트리기
        explode(bomb, ground)

        # 다음에 터트릴 폭탄 찾기
        for i in range(r):
            for j in range(c):
                if ground[i][j] == 'O':
                    bomb.append((i,j))
    
    else :
        # 폭탄 모두 설치
        ground = [['O']*c for _ in range(r)]


for i in range(1, n+1):
    simulate(i)

for i in ground:
    print(''.join(i))