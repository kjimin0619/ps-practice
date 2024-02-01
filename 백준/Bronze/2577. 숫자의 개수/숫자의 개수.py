a = int(input())
b = int(input())
c = int(input())

info = [0] * 10
result = a * b * c
strResult = str(result)

for strI in strResult:
  idx = int(strI)
  info[idx] += 1

for i in info:
  print(i)
