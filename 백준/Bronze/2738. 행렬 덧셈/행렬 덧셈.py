n,m = map(int, input().split())

a1 = []
for _ in range(n):
    a1.append(list(map(int, input().split())))
    
a2 = []
for _ in range(n):
    a2.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        print(a1[i][j] + a2[i][j], end=' ')
    print()