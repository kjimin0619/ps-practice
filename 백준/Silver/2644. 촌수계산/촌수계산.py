from sys import stdin as s
from collections import deque
n = int(s.readline().strip())
start, end = map(int,s.readline().split())
m = int(s.readline().strip())
relation = [[]*(n+1) for _ in range(n+1)]

# 관계 그래프 형성
for _ in range(m):
    parent, child = map(int,s.readline().split())
    relation[child].append(parent)
    relation[parent].append(child)

def dfs(start, end):
    relate_count = [0]*(n+1)
    visited = [False]*(n+1)
    stack = deque([start])
    while stack:
        now = stack.pop()
        one_relation = relation[now]
        for f in one_relation:
            if visited[f] == False :
                relate_count[f] = relate_count[now] + 1
                stack.append(f)
                visited[f] = True
    return relate_count

result = dfs(start,end)
if result[end] == 0 :
    print(-1)
else :
    print(result[end])
