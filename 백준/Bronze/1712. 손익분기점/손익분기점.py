import sys
# A = 고정비용, B = 가변비용, C = 노트북 가격
A, B, C = map(int, sys.stdin.readline().split())
# 손익분기점 : 수입 > 고정비용 + 가변비용 == cx > a + bx
if B >= C : 
    print(-1)
else : 
    print(A//(C-B)+1)