from sys import stdin as s
#s = open("input.txt","rt")
n = int(s.readline().strip())
start, end = map(int,s.readline().split())
m = int(s.readline().strip())
relation = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
res = [] # 탐색 횟수

# 관계 그래프 형성
for _ in range(m):
    parent, child = map(int,s.readline().split())
    relation[child].append(parent)
    relation[parent].append(child)


def dfs(start,cnt):
    visited[start] = True
    cnt += 1

    if start == end :
        res.append(cnt)
        
    for i in relation[start]:
        if not visited[i]:
            dfs(i, cnt)

dfs(start,-1)
if len(res) == 0 : print(-1)
else : print(res[0])
