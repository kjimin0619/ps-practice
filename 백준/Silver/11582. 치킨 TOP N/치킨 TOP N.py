# 11582
n = int(input())  # 치킨집 수
scores = list(map(int, input().split()))
k = int(input())  # 정렬 회원수

idx = n // k

for i in range(0, n, idx):
    arr = scores[i:i + idx]
    arr.sort()
    for a in arr:
        print(a, sep=' ', end=' ')