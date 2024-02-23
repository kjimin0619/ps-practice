from sys import stdin as s
n = int(s.readline().strip())  # 탑의 개수
tops = list(map(int, s.readline().split()))  # 탑 높이 정보
answer = [0] * n  # 결과
stack = []  # 스택 초기화 (높이, 탑 순서)

for i in range(n):
  while stack:
    # 현재 송신탑보다 작은 탑들은 쓸모 없음 -> 제거
    if (tops[i] > stack[-1][0]):
      stack.pop()
    else:
      # 수신탑 정보 저장
      answer[i] = stack[-1][1]
      break
  stack.append((tops[i], i + 1))

print(*answer)