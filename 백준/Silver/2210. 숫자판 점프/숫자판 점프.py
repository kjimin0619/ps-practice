from sys import stdin as s
board = []
direction = [(-1,0),(1,0),(0,-1),(0,1)]
nums = set()
             
for i in range(5):
    n = s.readline().split()
    board.append(n)

def dfs(x,y,number):
    if len(number) == 6 :
        nums.add(number)
        return
    
    for (_x,_y) in direction :
        if (0<= _x + x < 5) and (0<= _y + y < 5):
            new_x, new_y = _x + x, _y + y
            dfs(new_x, new_y, number+board[new_x][new_y])

for i in range(5):
    for j in range(5):
        start = (i,j)
        dfs(i,j,board[i][j])

print(len(nums))