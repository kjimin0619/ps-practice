import sys
input = sys.stdin.readline

m = int(input()) # 붙일 색종이 수

arr = [[0]*100 for _ in range(100)]
for _ in range(m) : # 입력받은 색종이 수만큼
    y1, x1 = map(int, input().split()) # 좌표 입력  
    
    # 가로 
    for i in range(x1, x1+10) :
        # 세로  
        for j in range(y1, y1+10) :
            arr[i][j] = 1
            
result = 0 
for k in range(100) :
    result += arr[k].count(1)
print(result)