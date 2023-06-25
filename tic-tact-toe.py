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
# function to validate players move on the board
def validate_move(position):
    if position < 1 or position > 9:
        return False
    # calculating corresponding row and column indices
    row = (position - 1) // 3
    column = (position -1) % 3
    
    # checking if the corresponding position is empty
    if board[row][column] != '':
        return False
    
    return True
    

    