"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_X = 0
    number_O = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                number_X += 1
            elif board[i][j] == O:
                number_O += 1
            else:
                continue
    if number_X == number_O:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    posicoes = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
            # Armazena as coordenadas da posição
                posicoes.add((i, j))
    return posicoes
 



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = copy.deepcopy(board)
    if action not in actions(board):
        raise Exception("This action is not valid.")
    new_board[i][j] = player(board)
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board: #Analisa as linhas
        if None not in row and row.count('X') == len(row):
            return X
        if None not in row and row.count('O') == len(row):
            return O
        
    for j in range(len(board[0])): #Analisa as colunas
        column = [board[i][j] for i in range(len(board))]
        if None not in column and column.count('X') == len(column):
            return X
        if None not in column and column.count('O') == len(column):
            return O
        
    diagonal1 = [board[i][i] for i in range(len(board))] #Analisa a diagonal principal
    if None not in diagonal1 and diagonal1.count('X') == len(diagonal1):
        return X
    if None not in diagonal1 and diagonal1.count('O') == len(diagonal1):
        return O
    
    diagonal2 = [board[i][len(board)-i-1] for i in range(len(board))] #Analisa a diagonal secundaria
    if None not in diagonal2 and diagonal2.count('X') == len(diagonal2):
        return X
    if None not in diagonal2 and diagonal2.count('O') == len(diagonal2):
        return O
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    none_value = False
    for row in board:
        for element in row:
            if element is None:
                none_value = True
                break
        if none_value:
            break
    if winner(board) in [X,O] or none_value == False:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1 
        else:
            return 0
    else:
        return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    actual_player = player(board)
    if terminal(board) == True:
        return None
    else:
        def max_Value(board):
            if terminal(board):
                return utility(board)
            v = -math.inf
            for action in actions(board):
                v = max(v, min_Value(result(board,action)))
            return v
        
        def min_Value(board):
            if terminal(board):
                return utility(board)
            v = math.inf
            for action in actions(board):
                v = min(v, max_Value(result(board,action)))
            return v

        if actual_player == X:
            best_score = -math.inf
            best_action = None
            for action in actions(board):
                score = min_Value(result(board, action))
                if score > best_score:
                    best_score = score
                    best_action = action

            return best_action
        

        if actual_player == O:
            best_score = math.inf
            best_action = None
            for action in actions(board):
                score = max_Value(result(board, action))
                if score < best_score:
                    best_score = score
                    best_action = action
            return best_action