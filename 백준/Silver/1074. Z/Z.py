# 11582
n, r, c = map(int, input().split())  # 배열 사이즈 크기, 행, 렬
count = 0

while n!=0:
  n = n -1
  size = 2**n

  # 1사분면
  if r < size and c < size :
    count += 0
  
  # 2사분면
  elif r < size and c >= size :
    count += size *size
    c = c - size
    
  # 3사분면
  elif r >= size and c < size :
    count += size * size * 2
    r = r - size
    
  # 4사분면
  else :
    count += size * size * 3
    c = c - size
    r = r - size

print(count)