import sys
t = int(input()) # 테스트 케이스

for i in range(t) :
    w,h,n = map(int, sys.stdin.readline().split()) # 층 수, 방 수, 손님번호
    x = w if (n % w == 0) else (n % w) # 층
    y = (n-1)//w + 1 # 호
    print("{}{:02d}".format(x,y))
