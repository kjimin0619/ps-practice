def isHansu(n):
    # 1,2자리 수는 무조건 한수
    if n < 100 : return True
    else : # 세 자리수. 1000은 자동으로 False 됨됨
        num = list(map(int,str(n)))
        if num[0] - num[1] == num[1] - num[2] : return True
        else : return False
        
n = int(input())
cnt = 0
for i in range(1,n+1):
    if (isHansu(i)) : 
        cnt += 1
print(cnt)