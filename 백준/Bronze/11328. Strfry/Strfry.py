tc = int(input())
for _ in range(tc):
  origin, target = map(list, input().split())

  origin.sort()
  target.sort()
  flag = 1
    
  for i in range(len(origin)):
    if origin[i] != target[i]:
      flag = 0
      break

  if flag:
    print("Possible")
  else:
    print("Impossible")
