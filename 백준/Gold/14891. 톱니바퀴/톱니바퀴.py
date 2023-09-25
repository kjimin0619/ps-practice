from sys import stdin as s
from collections import deque

wheels = []
for _ in range(4):
    wheels.append(deque(list(map(int, s.readline().strip()))))
wheels.insert(0,[])

k = int(s.readline().strip())
rotate = []
for i in range(k) :
    rotate.append(list(map(int, s.readline().split())))
    
# 바퀴 돌리기
# 왼쪽
def rleft(wn, dirc, d) :
    if wn != 1 :
        if d != wheels[wn-1][2] :
            temp = wheels[wn-1][6]
            wheels[wn-1].rotate(dirc*(-1))
            # 왼쪽의 왼쪽도 돌리기
            rleft(wn-1, dirc *(-1), temp)

# 오른쪽
def rright(wn, dirc, d) :
    if wn != 4 :
        if d != wheels[wn+1][6] :
            temp =  wheels[wn+1][2]
            wheels[wn+1].rotate(dirc*(-1))
            # 오른쪽의 오른쪽 돌리기
            rright(wn+1, dirc*(-1),temp)
            
for n,d in rotate :
    curleft = wheels[n][6]
    curright = wheels[n][2]
    wheels[n].rotate(d)
    rleft(n, d, curleft)
    rright(n, d, curright)
    
    
res = 0
for i in range(1,5) :
    res += wheels[i][0]*(2**(i-1))
print(res)