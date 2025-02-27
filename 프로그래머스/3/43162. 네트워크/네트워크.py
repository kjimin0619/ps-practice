def solution(n, computers):
    def dfs(node, visited, computers):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in range(n):
                if computers[current][neighbor] == 1 and visited[neighbor] == 0 :
                    visited[neighbor] = 1
                    stack.append(neighbor)
    visited = [0] * n
    answer = 0
    for i in range(n):
        if visited[i] == 0 :
            visited[i] = 1 # 방문 처리
            dfs(i, visited, computers)
            answer += 1
        
        
    return answer

