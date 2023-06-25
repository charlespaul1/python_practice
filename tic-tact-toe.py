# creating the tic tac toe program
# initializing the board
board = [[' 'for _ in range(3)] for _ in range(3)]

# displaying the board
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)
    