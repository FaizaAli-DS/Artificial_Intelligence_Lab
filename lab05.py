import heapq, itertools

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = {'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1}

def neighbours(state):
    i = state.index(0); r, c = divmod(i, 3)
    for a, d in MOVES.items():
        if (a == 'Up' and r == 0) or (a == 'Down' and r == 2) \
           or (a == 'Left' and c == 0) or (a == 'Right' and c == 2):
            continue
        s = list(state); j = i + d
        s[i], s[j] = s[j], s[i]
        yield a, tuple(s)

def manhattan(state):
    """Sum of distances of each tile from its goal position."""
    dist = 0
    for idx, tile in enumerate(state):
        if tile == 0:
            continue
        goal_idx = tile - 1
        dist += abs(idx // 3 - goal_idx // 3) + abs(idx % 3 - goal_idx % 3)
    return dist

def best_first(start, f_type):
    """Generic best-first search.
    f_type = 'greedy' -> f(n) = h(n)
    f_type = 'astar'  -> f(n) = g(n) + h(n)"""
    counter = itertools.count()          # tie-breaker for the heap
    h0 = manhattan(start)
    frontier = [(h0, next(counter), 0, start, [])]
    best_g = {start: 0}
    expanded = 0
    while frontier:
        f, _, g, state, path = heapq.heappop(frontier)
        if state == GOAL:
            return path, expanded
        expanded += 1
        for action, child in neighbours(state):
            g2 = g + 1
            if child not in best_g or g2 < best_g[child]:
                best_g[child] = g2
                h = manhattan(child)
                f2 = h if f_type == 'greedy' else g2 + h
                heapq.heappush(frontier, (f2, next(counter), g2, child, path + [action]))
    return None, expanded

start = (8, 1, 3,
         4, 0, 2,
         7, 6, 5)
print("Start h(n) =", manhattan(start))
print(f"{'Algorithm':<10}{'Solution length':>17}{'Nodes expanded':>17}")
for name in ['greedy', 'astar']:
    path, exp = best_first(start, name)
    print(f"{name:<10}{len(path):>17}{exp:>17}")
path, _ = best_first(start, 'astar')
print("A* moves:", ' '.join(path))
