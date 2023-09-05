from heapq import heappush, heappop

def solution(n, k, enemy):
    q = []
    for r, e in enumerate(enemy) :
        heappush(q, e)
        
        if len(q) > k :
            n = n - heappop(q)
        if n < 0 :
            return r
    return len(enemy)
    
        
