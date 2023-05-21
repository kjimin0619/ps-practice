n = int(input())
board = [0] * n
cnt = 0

def is_promising(x):
    for i in range(x):
        if(board[i] == board[x] or abs(board[x] - board[i]) == abs(x - i)):
            return False
    return True


def n_queens(x):
    global cnt
    if x == n :
        cnt += 1
        return

    else :
        for i in range(n):
            board[x] = i
            if is_promising(x):
                n_queens(x+1)
            board[x] = 0

n_queens(0)
print(cnt)