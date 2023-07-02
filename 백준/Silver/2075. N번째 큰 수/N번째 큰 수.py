from sys import stdin as s
import heapq

q = []
n = int(s.readline())

for i in range(n):
    nums = list(map(int,s.readline().split()))
    if not q :
        for n in nums :
            heapq.heappush(q, n)
    else :
        for n in nums :
            temp = heapq.heappop(q)
            if n > temp :
                heapq.heappush(q, n)
            else :
                heapq.heappush(q,temp)
                
print(heapq.heappop(q))