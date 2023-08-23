
def bingo(player, board):
    # row 검사
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
    # col 검사
    for j in range(3):
        if all (board[i][j] == player for i in range(3)) :
            return True
    # diagonal 검사
    if all (board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
  
          
def solution(board):
    cnt_o = sum(row.count("O") for row in board)
    cnt_x = sum(row.count("X") for row in board)

    if cnt_x > cnt_o or abs(cnt_x - cnt_o) > 1 :
        return 0
    
    else :
        if bingo("O", board) and cnt_o - cnt_x != 1 :
            return 0
        if bingo("X", board) and cnt_o != cnt_x :
            return 0
    return 1
        
 
    return 1