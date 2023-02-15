t = int(input())

for _ in range(t):
    floor = int(input()) # 층
    n = int(input()) # 호

    f0 = [x for x in range(1,n+1)] # 0층 거주인원 
    # 층 수 만큼 반복
    for k in range(floor) : 
        # 한 층 마다
        for i in range(1,n):
            f0[i] = f0[i] + f0[i-1] # 층 별 호실 인원 수 변경
            
    print(f0[-1]) # 가장 마지막 수(n호실 인원) 출력