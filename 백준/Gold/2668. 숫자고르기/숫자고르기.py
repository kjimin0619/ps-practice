from sys import stdin as s
from collections import deque

n = int(s.readline())
# 연결 리스트
graph = [[] for _ in range(n+1)]
for i in range(n) :
    graph[i+1] = int(s.readline())

def find_path(start) :
    q = deque([start])
    visited = [False] * (n+1)
    path = []
    
    while q :
        curr = q.pop()
        visited[curr] = True
        path.append(curr)
        next = graph[curr]
        if visited[next] == False :
            visited[next] = True
            q.append(next)
    path.append(next)
    return path

start = set()
end = set()

for i in range(1,n+1):
    temp = find_path(i)
    if temp[0] == temp[-1] :
        for item in temp :
            start.add(item)

print(len(start))
for i in sorted(list(start)):
    print(i)