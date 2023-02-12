n = int(input())
house = 1 # 벌집의 개수
cnt = 1

while n > house :
    house = house + cnt*6
    cnt += 1
print(cnt)
