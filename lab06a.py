import random

N = 8

def attacking_pairs(board):
    """board[c] = row of the queen in column c. Count pairs that attack."""
    h = 0
    for c1 in range(N):
        for c2 in range(c1 + 1, N):
            if board[c1] == board[c2] or abs(board[c1] - board[c2]) == c2 - c1:
                h += 1
    return h

def best_neighbour(board):
    """Try moving each queen to every other row in its column."""
    best, best_h = None, attacking_pairs(board)
    for col in range(N):
        for row in range(N):
            if row == board[col]:
                continue
            nb = list(board); nb[col] = row
            h = attacking_pairs(nb)
            if h < best_h:
                best, best_h = nb, h
    return best, best_h

def hill_climbing(board):
    steps = 0
    while True:
        nb, h = best_neighbour(board)
        if nb is None:                 # no better neighbour -> local optimum
            return board, attacking_pairs(board), steps
        board, steps = nb, steps + 1

def random_restart(max_restarts=100):
    for r in range(max_restarts):
        start = [random.randrange(N) for _ in range(N)]
        board, h, steps = hill_climbing(start)
        if h == 0:
            return board, r + 1
    return None, max_restarts

random.seed(3)
start = [random.randrange(N) for _ in range(N)]
board, h, steps = hill_climbing(start)
print("Start board :", start, "h =", attacking_pairs(start))
print("Hill climb  :", board, "h =", h, "after", steps, "steps")

# Success rate of plain hill climbing over 200 random boards
wins = sum(hill_climbing([random.randrange(N) for _ in range(N)])[1] == 0 for _ in range(200))
print(f"Plain hill climbing success rate: {wins/200:.0%}")

sol, restarts = random_restart()
print("Random-restart solution:", sol, "found after", restarts, "restart(s)")
for r in range(N):
    print(' '.join('Q' if sol[c] == r else '.' for c in range(N)))
