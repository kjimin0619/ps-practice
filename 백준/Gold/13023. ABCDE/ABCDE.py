import sys
from sys import stdin as s
sys.setrecursionlimit(10**6)

result = 0
n, m = map(int, s.readline().split())
network = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a,b = map(int, s.readline().split())
    network[a].append(b)
    network[b].append(a)

def dfs(start, cnt):
    global result
    visited[start] = True
    cnt +=1
    
    if  cnt == 5:
        result = 1
        return 
    
    for f in network[start]:
        if visited[f] == False :
            visited[f] = True
            dfs(f, cnt)
            
    visited[start] = False
    
for i in range(n):
    if result == 1 :
        break
    
    dfs(i, 0)
    
print(result)