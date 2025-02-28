from collections import deque
def solution(begin, target, words):
    
    n =  len(words) # 단어 갯수
    visited = [False]*n
    
    def bfs(node, visited, words) :
        d = deque([(node,0)])
        answer = 0
        while d :
            cur, cnt = d.popleft()
            if cur == target :
                return cnt
                
            for i in range(n) :
                # 방문 안한 단어 중
                if visited[i] == False :
                    c = 0
                    # 바꿀 수 있는지 검사하기
                    for a,b in zip(cur, words[i]) :
                        if a!=b : c += 1
                    if c == 1 :
                        # 바꿀 수 있는 단어 발견
                        d.append((words[i], cnt+1))
                        visited[i] = True
                
        return 0
                
    answer = bfs(begin, visited, words)       
    return answer