# 9x9 행렬 입력 -> 최댓값과 위치(행 열) 출력
import sys
input = sys.stdin.readline

ans, x, y = -1, 0, 0
for i in range(9):
    arr = list(map(int, input().split()))
    # 행 크기 비교 
    if max(arr) > ans :
        ans = max(arr)
        x = i+1 # 행
        y = arr.index(ans) + 1 # 열
        
print(ans)
print(x, y)