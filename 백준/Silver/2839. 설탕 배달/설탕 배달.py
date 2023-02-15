n = int(input())
cnt = 0   

while n >= 0:
    if n % 5 == 0 :
        cnt += (n//5)
        print(cnt)
        break
    n -= 3
    cnt += 1 # 남은 설탕이 5의 배수가 될 때까지 3키로씩 빼 감
else : print(-1)