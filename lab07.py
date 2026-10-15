import math

WIN_LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def winner(b):
    for a, c, d in WIN_LINES:
        if b[a] != ' ' and b[a] == b[c] == b[d]:
            return b[a]
    return None

def terminal(b):
    return winner(b) is not None or ' ' not in b

def utility(b):
    w = winner(b)
    return 1 if w == 'X' else -1 if w == 'O' else 0   # X = MAX, O = MIN

nodes = 0

def minimax(b, is_max):
    global nodes; nodes += 1
    if terminal(b):
        return utility(b)
    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X' if is_max else 'O'
            scores.append(minimax(b, not is_max))
            b[i] = ' '                                  # undo move
    return max(scores) if is_max else min(scores)

def alphabeta(b, is_max, alpha=-math.inf, beta=math.inf):
    global nodes; nodes += 1
    if terminal(b):
        return utility(b)
    if is_max:
        value = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                value = max(value, alphabeta(b, False, alpha, beta))
                b[i] = ' '
                alpha = max(alpha, value)
                if alpha >= beta:
                    break                                # beta cut-off
        return value
    else:
        value = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                value = min(value, alphabeta(b, True, alpha, beta))
                b[i] = ' '
                beta = min(beta, value)
                if alpha >= beta:
                    break                                # alpha cut-off
        return value

def best_move(b, player, search):
    best_i, best_v = None, (-math.inf if player == 'X' else math.inf)
    for i in range(9):
        if b[i] == ' ':
            b[i] = player
            v = search(b, player == 'O')
            b[i] = ' '
            if (player == 'X' and v > best_v) or (player == 'O' and v < best_v):
                best_i, best_v = i, v
    return best_i, best_v

def show(b):
    for r in range(3):
        print(' ' + ' | '.join(b[r*3:r*3+3]))
        if r < 2: print('---+---+---')

# Compare the two algorithms on the empty board
for name, algo in [('Minimax', minimax), ('Alpha-Beta', alphabeta)]:
    nodes = 0
    move, val = best_move([' '] * 9, 'X', algo)
    print(f"{name:<11} best first move = {move}, value = {val}, nodes searched = {nodes}")

# AI (X) vs AI (O) game using alpha-beta: perfect play ends in a draw
board = [' '] * 9; player = 'X'
while not terminal(board):
    move, _ = best_move(board, player, alphabeta)
    board[move] = player
    player = 'O' if player == 'X' else 'X'
show(board)
print("Result:", winner(board) or "Draw")
