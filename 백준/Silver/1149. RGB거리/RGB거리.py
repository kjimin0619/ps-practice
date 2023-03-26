import sys
input = sys.stdin.readline

N = int(input())
Houses = [list(map(int,input().split())) for _ in range(N)]
before_cost = [0,0,0]

for c in Houses :
    c[0] = c[0] + min(before_cost[1],before_cost[2])
    c[1] = c[1] + min(before_cost[0],before_cost[2])
    c[2] = c[2] + min(before_cost[0],before_cost[1])

    before_cost = c
  
print(min(before_cost))