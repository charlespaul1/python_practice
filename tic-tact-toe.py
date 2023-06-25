# creating the tic tac toe program
# initializing the board
board = [[' 'for _ in range(3)] for _ in range(3)]

# displaying the board
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)
# function to handle players move/ input
def players_move():
    position = input('Enter a position between 1- 9:  ')
    return int(position)
    