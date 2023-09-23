from sys import stdin as s

n = int(s.readline().strip())
liq = list(map(int,s.readline().split()))

left, right = 0, n-1

ans = abs(liq[left] + liq[right])
aleft, aright = left, right

while left < right :
    tmp = liq[left] + liq[right]
    
    if abs(tmp) < ans :
        aleft = left
        aright = right
        ans = abs(tmp)
        
        if ans == 0:
            break
    
    if tmp < 0 :
        left += 1
    else :
        right -= 1

print(liq[aleft], liq[aright])
    