from collections import deque
import time

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)          # 0 represents the blank tile

MOVES = {'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1}

def actions(state):
    """Return the legal moves of the blank tile."""
    i = state.index(0)
    row, col = divmod(i, 3)
    legal = []
    if row > 0: legal.append('Up')
    if row < 2: legal.append('Down')
    if col > 0: legal.append('Left')
    if col < 2: legal.append('Right')
    return legal

def result(state, action):
    """Transition model: swap the blank with the neighbouring tile."""
    i = state.index(0)
    j = i + MOVES[action]
    s = list(state)
    s[i], s[j] = s[j], s[i]
    return tuple(s)

def goal_test(state):
    return state == GOAL

def is_solvable(state):
    tiles = [t for t in state if t != 0]
    inversions = sum(1 for a in range(len(tiles))
                       for b in range(a + 1, len(tiles)) if tiles[a] > tiles[b])
    return inversions % 2 == 0

def solve_bfs(start):
    frontier = deque([(start, [])])
    explored = {start}
    expanded = 0
    while frontier:
        state, path = frontier.popleft()
        if goal_test(state):
            return path, expanded, len(explored)
        expanded += 1
        for a in actions(state):
            child = result(state, a)
            if child not in explored:
                explored.add(child)
                frontier.append((child, path + [a]))
    return None, expanded, len(explored)

def show(state):
    for r in range(3):
        print(' '.join(str(x) if x else '_' for x in state[r*3:r*3+3]))

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)
print("Start state:"); show(start)
print("Solvable:", is_solvable(start))
t0 = time.perf_counter()
path, expanded, generated = solve_bfs(start)
t1 = time.perf_counter()
print("Solution :", path)
print("Moves    :", len(path))
print("Nodes expanded :", expanded)
print("Nodes generated:", generated)
print(f"Time taken     : {(t1-t0)*1000:.2f} ms")
