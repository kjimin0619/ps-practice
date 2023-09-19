from sys import stdin as s
from itertools import combinations

N,M = map(int, s.readline().split())
board = []
chickens = []
houses = []

for i in range(N):
    temp =  list(map(int, s.readline().split()))
    board.append(temp)

    for j in range(N):
        if temp[j] == 2 :
            chickens.append((i,j))
        elif temp[j] == 1 :
            houses.append((i,j))

def cal_sec(comb) :
    res = 0
    for h in houses :
        mini = 1e9
        for x,y in comb :
            mini = min(mini, abs(x-h[0]) + abs(y-h[1]))
        res += mini
    return res

ans = 1e9
for i in combinations(chickens, M) :
    ans = min(ans, cal_sec(i))
print(ans)
    