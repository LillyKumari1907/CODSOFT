import math

# --- 1. Game Board Setup --- 
def print_board(board):
    """"Prints the current state of the Tic-Tac-Toe board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} \n---|---|---\n {board[3]} | {board[4]} | {board[5]} \n---|---|---\n {board[6]} | {board[7]} | {board[8]} \n")

def check_score(board):
    """Checks all 8 possible winning lines for a specific player."""
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            if board[condition[0]] == 'O':
                return 10 # AI wins
            elif board[condition[0]] == 'X':
                return -10 # Human wins
    if ' ' not in board:
        return 0 # Tie
    return None # Game is still going
            
# ---  2. The AI Brain (Minimax Algorithm) ---
def minimax(board, depth, is_maximizing):
    score = check_score(board)

    # Base cases: Someone won, or it's a tie
    if score is not None:
        return score
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range (9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
        
def ai_best_move(board):
    """Finds the ultimate best move for the AI """
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)                
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def main():
    """ The main interactive game loop """
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. Enter a number 0-8 to play.")
     
    #Show a guide board with numbers
    print_board([str(i) for i in range(9)])

    while True:
        # 1. Human Turn
        while True:
            try:
                move = int(input("Enter your move (0-8): "))
                if move >= 0 and move <= 8 and board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("Spot taken or invalid! Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")  
        print_board(board)      

        # Check if human  won or tied
        if check_score(board) is not None:
            break
       
         # 2. --- AI Turn ---
        print("AI is the calculating...")
        ai_move = ai_best_move(board)
        board[ai_move] = 'O'

        print(f"AI chose spot {ai_move}")
        print_board(board)

        # Check if AI won or tied
        if check_score(board) is not None:
            break
    # 3. GAME OVER SCREEN
    result = check_score(board)
    if result == 10:
        print("Game Over: AI wins!")
    elif result == -10:
        print("Game Over: You win!")
    else:
        print("Game Over: It's a Tie! ")
        
#start the game        
if __name__== "__main__":
    main() 
