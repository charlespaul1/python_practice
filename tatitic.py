# initializing the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# displaying the board
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)
    
# players move
def player_move():
    position = int(input('Enter a position beetween 1- 9:'))
    return position

# validating players move
def is_valid_move(position):
    if position < 1 or position > 9:
        return False
    
    # calculate the row and column indices
    row = (position -1)  // 3
    column = (position - 1) % 3
    
    # check if corresponding indices is empty
    if board[row][column] != ' ':
        return False
    return True

# updating the board
def updating_board(position, symbol):
    row = (position - 1) // 3
    column = (position - 1) % 3
    
    board[row][column] = symbol
    
# check for a win
def check_win(symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    # check column
    for column in range(3):
        if all(board[row][column] == symbol for row in range(3)):
            return True
            
    # check diagonal 
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

# implementing the game
current_player = 'X'
while True:
    display_board()
    position = player_move()
    
    if not is_valid_move(position):
        print("Invalid move Try again!!")
        continue
    updating_board(position, current_player)
    
    if check_win(current_player):
        display_board()
        print(f"{current_player}, has won")
        break
        
        if all(cell != ' ' for row in board for cell in row):
            display_board()
            print("It's a tie!!")
            break
    # switch players
    current_player = 'O' if current_player == 'X' else 'X'
        


    
    
    
    
    
    
