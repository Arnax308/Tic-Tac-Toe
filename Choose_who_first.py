import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player1'
    else:
        return 'Player2'