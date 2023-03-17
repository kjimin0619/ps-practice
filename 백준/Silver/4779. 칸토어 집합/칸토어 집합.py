def solve(le, cnt):
  if cnt <= 1:
    return le
  length = cnt // 3  # 그룹 당 길이
  left = le[:length]
  middle = ' ' * length
  right = le[2 * length:]
  return solve(left, length) + middle + solve(right, length)


# 사용자 입력 반복
while True:
  try:
    n = input()
    if n == '':
      break
    else:
      n = int(n)
      letters = "-" * (3**n)
      print(solve(letters, 3**n))

  except EOFError:
    break