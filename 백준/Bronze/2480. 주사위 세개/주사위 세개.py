import sys

a, b, c = map(int, sys.stdin.readline().split(" "))

if (a == b and a == c):
  print(a * 1000 + 10000)
elif (a != b and a != c and b != c):
  print(max([a, b, c]) * 100)
else :
  if (a == b or a == c ) :
    print(1000 + 100*a)
  else :
    print(1000 + 100*c)
  