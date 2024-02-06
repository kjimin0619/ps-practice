import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
  op = list(sys.stdin.readline().split())
  match op[0] :
    case 'push' :
      stack.append(int(op[1]))
    case 'top' :
      print(stack[-1]) if stack else print("-1")
    case 'pop':
      print(stack.pop()) if stack else print('-1')
    case 'empty':
      print("0") if stack else print("1")
    case 'size':
      print(len(stack))
    
