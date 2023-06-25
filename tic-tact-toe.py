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
def valid_move(position):
    if position < 1 or position > 9:
        return False
    # calculating corresponding row and column indices
    row = (position - 1) // 3
    column = (position - 1) % 3
    
    # checking if the corresponding position is empty
    if board[row][column] != ' ':
        return False
    
    return True
# updating the board
def update_board(position, symbol):
    row = (position - 1) // 3
    column = (position - 1) % 3
    
    board[row][column] = symbol
    
# checking for a win
def check_win(symbol):
    # checking for a win in the rows on the board
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    # checking the columns for a win
    for column in range(3):
        if all (board[row][column] == symbol for row in range(3)):
            return True
        
    # checking diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

# implementing the gaming loop
current_player = 'X'
 
while True:
    display_board()
    position = players_move()
    
    if not valid_move(position):
        print("Invalid Move, Try again")
        continue
        
    update_board(position, current_player)
    
    if check_win(current_player):
        display_board()
        print(f"{current_player}, has won")
        break
    # checking for a tie
    if all(cell != ' ' for row in board for cell in row):
        display_board()
        print("It's a tie!!")
        break
    # switch players
    current_player = 'O' if current_player == 'X' else 'X'
        

    