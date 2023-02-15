import sys
a,b,v = map(int, sys.stdin.readline().split())
# 올라가는 데 걸린 일수 = d, 올라간 높이 = h
# h = ad - b(d-1) >= v --> d >= (v-b)/(a-b)
d = (v-b)/(a-b) # 올라가는데 걸린 일수 
print(int(d) if d == int(d) else int(d)+1)