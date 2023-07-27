from copy import deepcopy

N = int(input())
small_jump = []
big_jump = []

for _ in range(N-1):
    small, big = map(int, input().split())
    small_jump.append(small)
    big_jump.append(big)
very_big_jump = int(input())

if N >= 3: # 일반적인 케이스
    DP1 = [0 for _ in range(N)]
    DP1[0] = 0
    DP1[1] = small_jump[0]
    for i in range(2, N):
        DP1[i] = min(DP1[i-2] + big_jump[i-2], DP1[i-1] + small_jump[i-1])
    energy_list = [DP1[N-1]]
    for k in range(N-3):
        DP2 = deepcopy(DP1)
        DP2[k+3] = DP1[k] + very_big_jump  # k번째 돌에서 슈퍼점프
        for i in range(k+4, N):
            DP2[i] = min(DP2[i-2] + big_jump[i-2], DP2[i-1] + small_jump[i-1])
        energy_list.append(DP2[N-1])
    print(min(energy_list))
elif N == 3:
    print(min(sum(small_jump), big_jump[0]))
elif N == 2:
    print(small_jump[0])
else:
    print(0)