def bingo(target, board):
    # 가로
    for i in range(3):
        if all(cell == target for cell in board[i]) :
            return True
    # 세로
    for i in range(3):
        if all(board[j][i] == target for j in range(3)) :
            return True
    
    # 대각선
    if all(board[i][i] == target for i in range(3)) :
        return True
        
    if all(board[i][2-i] == target for i in range(3)) :
        return True
    
    return False

def solution(board) :
    print("board : ",board)
    o_cnt, x_cnt = 0,0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O" :
                o_cnt += 1
            elif board[i][j] == "X" :
                x_cnt += 1
                
    # 선공, 후공 실수
    if x_cnt > o_cnt or abs(x_cnt - o_cnt) > 1:
        return 0
    
    # o 빙고
    if bingo("O",board) and x_cnt == o_cnt :
        return 0
    
    # x 빙고
    if bingo("X", board) and x_cnt == o_cnt - 1 :
        return 0
    return 1