from Check_Space import space_check
def player_choice(board):
   
    position = 0
   
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Please choose a position between 1 and 9 : '))
       
    return position