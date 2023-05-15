from sys import stdin as s

#s = open("input.txt","rt")

total = 0
n = int(s.readline())
m = int(s.readline())
g = []
parent = [i for i in range(n+1)]

for _ in range(m):
    n1,n2,cost = map(int, s.readline().split())
    g.append([cost,[n1,n2]])

g.sort(key = lambda x:x[0])

def findParent(a):
    if a == parent[a]:
        return a
    parent[a] = findParent(parent[a])
    return parent[a]

def union(a,b):
    a = findParent(a)
    b = findParent(b)
    # 번호가 큰 노드를 부모로 설정
    if b < a :
        parent[a] = b
    else :
        parent[b] = a

for cost, n in g:
    a,b = n[0],n[1]
    if findParent(a) != findParent(b):
        union(a,b)
        total = total + cost

print(total)