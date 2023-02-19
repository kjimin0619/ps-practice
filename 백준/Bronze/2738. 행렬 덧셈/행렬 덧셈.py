import sys
input = sys.stdin.readline

n,m = map(int, input().split())

a1 = [list(map(int, input().split())) for _ in range(n)]
a2 = [list(map(int, input().split())) for _ in range(n)]
    
for i in range(n):
    for j in range(m):
        print(a1[i][j] + a2[i][j], end=' ')
    print()