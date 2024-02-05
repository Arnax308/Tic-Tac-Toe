from Check_Space import space_check

def full_board_check(board):
    for n in range(1,10):
        if space_check(board,n) == True:
            return False
       
    return True