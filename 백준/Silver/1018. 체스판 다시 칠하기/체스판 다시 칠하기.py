from sys import stdin as s

n,m = map(int, s.readline().split())
board = []
for i in range(n):
    board.append(list(s.readline().strip()))
cut = []
col = m-8 + 1
row = n-8 + 1

def bfs(temp, color) :
    a = 0
    if temp[0][0] != color :
        a += 1
        
    for i in range(1,8) :
        for j in range(i+1):
            r = j
            c = i - j
            if i%2 == 0 :
                if temp[r][c] != color :
                    a += 1
            else :
                if temp[r][c] == color :
                    a += 1
    
    b = 0
    for i in range(1,8):
        for j in range(8-i):
            r = i + j
            c = 7 - j
            if i%2 == 0 :
                if temp[r][c] == color :
                    b += 1
            else :
                if temp[r][c] != color :
                    b += 1
           
    return a + b                   

for i in range(row):
    for j in range(col) :
        temp = board[i:i+8]
        temp = [row[j:j+8] for row in temp]
        cut.append(bfs(temp,"B"))
        cut.append(bfs(temp,"W"))
print(min(cut))
        
        