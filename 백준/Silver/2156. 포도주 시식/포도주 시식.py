from sys import stdin as s
n = int(s.readline())
grape = [int(s.readline()) for _ in range(n)]
max_grape = [0 for _ in range(n)]

if len(grape) == 1 :
    print(grape[0])
elif len(grape) == 2:
    print(grape[0]+grape[1])
else :
    max_grape[0] = grape[0]
    max_grape[1] = grape[0] + grape[1]
    max_grape[2] = max(grape[0]+grape[1], 
                        grape[1] + grape[2],
                        grape[0]+grape[2])
    for i in range(3,n):
        # i번째 포도주를 먹는 경우, 먹지 않는 경우
        # i번째 포도주를 먹는다면, 이전 포도주를 먹는 경우, 먹지 않는 경우
        # i번째 포도주 X : max_grape[i-1]
        # i번째 포도주 O & i-1번째 포도주 O : grape[i]+grape[i-1]+max_grape[i-3]
        # i번째 포도주 O & i-1번째 포도주 X : grape[i]+max_grape[i-2]
        max_grape[i] = max(max_grape[i-1],
                        grape[i]+grape[i-1]+max_grape[i-3],
                        grape[i]+max_grape[i-2])
    print(max(max_grape))