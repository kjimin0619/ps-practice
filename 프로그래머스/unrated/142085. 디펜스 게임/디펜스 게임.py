from heapq import heappop, heappush

def solution(n,k, enemy):
    h = []
    
    for r, e in enumerate(enemy):
        heappush(h, e)
        
        if len(h) > k :
            n = n - heappop(h)
        if n < 0 :
            return r
    return len(enemy)