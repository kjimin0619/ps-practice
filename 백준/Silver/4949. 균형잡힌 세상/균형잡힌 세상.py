import sys
from collections import deque

while True:
  sentence = sys.stdin.readline()[:-1]
  # 검사 종료
  if sentence == ".":
    break

  # 검사 시작
  stack = []
  check = ["(", "[", ")", "]"]
  flag = True  # 오류 없음

  for w in sentence:
    if w in check:
      if w == "(" or w == "[":
        stack.append(w)
      else:
        # 스택이 비어있으면 오류
        if not stack:
          flag = False
          break

        # 괄호 쌍이 맞지 않으면 오류
        elif w == ")":
          if stack[-1] == "[":
            flag = False
            break
          else:
            stack.pop(-1)
        else:
          if stack[-1] == "(":
            flag = False
            break
          else:
            stack.pop(-1)

  # 스택이 비어있고, flag도 참이라면
  if flag and not stack:
    print("yes")

  # 스택에 원소가 남아있거나, flag가 거짓이라면
  else:
    print("no")
