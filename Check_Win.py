def win_check(board, marker):
   
    #right top to bottom
    if board[9] == board[6] == board[3] == marker:
        result = True

    #center top to bottom
    elif board[8] == board[5] == board[2] == marker:
         result = True
           
    #left top to bottom
    elif board[7] == board[4] == board[1] == marker:
        result = True

    #1st row left to right
    elif board[7] == board[8] == board[9] == marker:
        result = True
       
    #2nd row left to right
    elif board[4] == board[5] == board[6] == marker:
        result = True

    #3rd row left to right
    elif board[1] == board[2] == board[3] == marker:
        result = True

    #Diagonal : left upper to Right bottom
    elif board[7] == board[5] == board[3] == marker:
        result = True

    #Diagonal : Right upper to Left bottom
    elif board[9] == board[5] == board[1] == marker:
        result = True

    else:
        result = False
   

    #Returning the winning message
    return result