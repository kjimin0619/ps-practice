from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    
    # 그래프 생성 (알파벳 순 정렬)
    for src, dst in tickets:
        graph[src].append(dst)
    for key in graph :
        graph[key].sort() # 오름차순 저렬
    
    route = [] # 최종 경로
    
    def dfs(node):
        while graph[node] :
            nxt = graph[node].pop(0) # 다음 목저지 생성            
            dfs(nxt)
        route.append(node) # 더 이상 갈 곳 없을 때, 도착지 정보 저장
            
    dfs("ICN")
    # route는 도착지 순으로 기록됨    
    return route[::-1]