from collections import deque
import heapq

# ---------- Grid maze: S = start, G = goal, # = wall ----------
MAZE = ["S . . . . # #",
        "# # . # # . .",
        ". . . # . . #",
        ". # . . . . #",
        ". . . . # . G"]
grid = [row.split() for row in MAZE]
ROWS, COLS = len(grid), len(grid[0])

def find(ch):
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == ch:
                return (r, c)

def neighbours(cell):
    r, c = cell
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:   # Up, Right, Down, Left
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != '#':
            yield (nr, nc)

def bfs(start, goal):
    frontier = deque([start]); parent = {start: None}; expanded = 0
    while frontier:
        node = frontier.popleft()                 # FIFO queue
        expanded += 1
        if node == goal:
            return build_path(parent, goal), expanded
        for nb in neighbours(node):
            if nb not in parent:
                parent[nb] = node
                frontier.append(nb)
    return None, expanded

def dfs(start, goal):
    frontier = [start]; parent = {start: None}; expanded = 0
    visited = set()
    while frontier:
        node = frontier.pop()                     # LIFO stack
        if node in visited:
            continue
        visited.add(node); expanded += 1
        if node == goal:
            return build_path(parent, goal), expanded
        for nb in neighbours(node):
            if nb not in visited:
                parent[nb] = node
                frontier.append(nb)
    return None, expanded

def build_path(parent, node):
    path = []
    while node is not None:
        path.append(node); node = parent[node]
    return path[::-1]

S, G = find('S'), find('G')
print(f"{'Algorithm':<6}{'Path length':>13}{'Nodes expanded':>17}")
for name, algo in [('BFS', bfs), ('DFS', dfs)]:
    path, exp = algo(S, G)
    print(f"{name:<6}{len(path)-1:>13}{exp:>17}")

# ---------- Uniform Cost Search on a weighted graph ----------
graph = {
    'Islamabad':  {'Rawalpindi': 15, 'Murree': 60, 'Attock': 80},
    'Rawalpindi': {'Islamabad': 15, 'Chakwal': 90, 'Jhelum': 110},
    'Murree':     {'Islamabad': 60, 'Abbottabad': 65},
    'Attock':     {'Islamabad': 80, 'Peshawar': 100},
    'Chakwal':    {'Rawalpindi': 90, 'Lahore': 230},
    'Jhelum':     {'Rawalpindi': 110, 'Gujranwala': 110},
    'Gujranwala': {'Jhelum': 110, 'Lahore': 70},
    'Abbottabad': {'Murree': 65},
    'Peshawar':   {'Attock': 100},
    'Lahore':     {'Chakwal': 230, 'Gujranwala': 70},
}

def ucs(graph, start, goal):
    frontier = [(0, start, [start])]          # (path cost, node, path)
    explored = set(); expanded = 0
    while frontier:
        cost, node, path = heapq.heappop(frontier)   # lowest g(n) first
        if node in explored:
            continue
        explored.add(node); expanded += 1
        if node == goal:
            return path, cost, expanded
        for nb, w in graph[node].items():
            if nb not in explored:
                heapq.heappush(frontier, (cost + w, nb, path + [nb]))
    return None, float('inf'), expanded

path, cost, exp = ucs(graph, 'Islamabad', 'Lahore')
print("\nUCS path :", ' -> '.join(path))
print("UCS cost :", cost, "km | nodes expanded:", exp)
