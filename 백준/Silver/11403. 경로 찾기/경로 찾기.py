from sys import stdin as s

n = int(s.readline()) # 정점의 갯수
edges = []

for i in range(n):
    e = list(map(int, s.readline().split()))
    edges.append(e)

# 경로 탐색
for k in range(n):
    for i in range(n):
        for j in range(n):
            if edges[i][j] != 1 :
                if edges[i][k] + edges[k][j] == 2 :
                    edges[i][j] = 1

# 경로 출력
for i in range(n):
    for j in range(n):
        print(edges[i][j], end=" ")
    print()