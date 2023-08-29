from collections import deque
def solution(x, y, n):
    dist = [0] * 1000001
    q = deque()
    
    dist[x] = 1
    q.append(x)
    
    while q :
        cur_x = q.popleft()
        if 0 <= cur_x + n < 1000001 and dist[cur_x + n] == 0 :
            dist[cur_x + n] = dist[cur_x] + 1
            q.append(cur_x+n)
        if 0 <= cur_x * 2 < 1000001 and dist[cur_x * 2 ] == 0 :
            dist[cur_x * 2 ] = dist[cur_x] + 1
            q.append(cur_x * 2)
        if 0 <= cur_x * 3 < 1000001 and dist[cur_x * 3] == 0 :
            dist[cur_x * 3] = dist[cur_x] + 1
            q.append(cur_x * 3)
   

           
            
    return dist[y] - 1
