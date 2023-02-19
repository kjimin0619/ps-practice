# 9x9 행렬 입력 -> 최댓값과 위치(행 열) 출력
import sys
input = sys.stdin.readline

# 9x9 행렬 제작
nums = [list(map(int, input().split())) for _ in range(9)]
max_value = max(map(max, nums))
mi, mj = 0, 0

for i in range(9) :
    for j in range(9):
        if nums[i][j] == max_value :
            mi, mj = i, j
            break
print(max_value)
print(mi+1, mj+1)