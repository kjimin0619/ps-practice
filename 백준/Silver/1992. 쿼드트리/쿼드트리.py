N = int(input()) #NxN 행렬
numbers = []
for _ in range(N) :
    numbers.append(list(map(int,input())))
  
def is_all_same(a,b,l) :
    global numbers
    pvt = numbers[a][b]
    for i in range(a,a+l) :
        for j in range(b,b+l):
            if numbers[i][j] != pvt:
                return False
    return True
  
def solve(x,y,n):
    global numbers
    
    if n <= 1 :
        print(numbers[x][y],end="")
  
    elif is_all_same(x,y,n):
        print(numbers[x][y],end="")
    
    else :
        new_n = n // 2
        print("(",end='')
        solve(x,y,new_n) # 1사분면
        solve(x,y+new_n,new_n) #2
        solve(x+new_n, y, new_n) # 3
        solve(x+new_n,y+new_n,new_n) #4
        print(")",end='')
  
    return
  
solve(0,0,N)