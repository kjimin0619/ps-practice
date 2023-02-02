A,B,C = map(int, input().split())

if (A == B and A == C and B == C) :
    prize = 10000 + A*1000
elif (A != B and A != C and B != C) :
    prize = max(A,B,C)*100
else :
    # 2개는 같은 눈
    if (A == B or A == C) : prize = 1000 + 100*A
    else : prize = 1000 + 100*B    
    
print(prize)