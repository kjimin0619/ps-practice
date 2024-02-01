origin = list(input().strip())
target = list(input().strip())
newOrigin = origin[:]

for i in range(len(origin)):
  if origin[i] in target:
    newOrigin.remove(origin[i])
    target.remove(origin[i])

print(len(newOrigin) + len(target))
