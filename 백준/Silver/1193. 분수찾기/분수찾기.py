n = int(input())
line = 1 # 사선 라인

while(n > line) :
    n -= line
    line += 1
    
# 분모 + 분자 = line + 1    
if (line % 2 == 1): # 사선라인 홀수
    print(line+1-n,n,sep="/")

else : # 사선라인 짝수
    print(n,line+1-n,sep="/") 