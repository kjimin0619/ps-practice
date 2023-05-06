from sys import stdin as s
import heapq
#s = open("input.txt","rt")
N,D = map(int, s.readline().split())
graph = [[] for _ in range(D+1)]

# 그래프 정보 입력
# 다음 지점으로 1씩 움직이는 경우 추가 
# (다음 노드, 거리값)
for i in range(D):
    graph[i].append((i+1,1))
# 지름길 정보 입력
for _ in range(N):
    start, end, length = map(int, s.readline().split())
    if end > D :
        continue # 도착 지점보다 먼 지점은 넘기기

    graph[start].append((end,length))

# single source shortest path 정보 저장 테이블
inf = 987654321
distance = [inf] * (D+1)
distance[0] = 0 

q = []
heapq.heappush(q,(0,0)) # 시작 노드는 0 (우선순위=거리, 도착노드) 
while q:
    dist, now = heapq.heappop(q) # 현재 도착노드까지의 거리, 현재 도착 노드

    # distance에 기록된 거리보다 크면 업데이트 X
    if distance[now] < dist :
        continue 

    for connection in graph[now] :
        # connection[0] = 도착노드
        # connection[1] = 거리
        cost = dist + connection[1] # now까지 거리 + 그 다음노드까지 거리
        if (distance[connection[0]] > cost):
            distance[connection[0]] = cost
            heapq.heappush(q,(cost,connection[0]))
            
print(distance[D])