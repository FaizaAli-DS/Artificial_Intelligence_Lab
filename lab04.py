import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['K'],
    'G': [],
    'H': [], 'I': [], 'J': [], 'K': []
}

def dls(node, goal, limit, visited_order):
    """Recursive Depth-Limited Search.
    Returns 'found', 'cutoff' or 'failure'."""
    visited_order.append(node)
    if node == goal:
        return 'found'
    if limit == 0:
        return 'cutoff'
    cutoff_occurred = False
    for child in tree[node]:
        res = dls(child, goal, limit - 1, visited_order)
        if res == 'found':
            return 'found'
        if res == 'cutoff':
            cutoff_occurred = True
    return 'cutoff' if cutoff_occurred else 'failure'

def iddfs(start, goal, max_depth=10):
    """Iterative Deepening: call DLS with limit 0, 1, 2, ..."""
    for depth in range(max_depth + 1):
        order = []
        res = dls(start, goal, depth, order)
        print(f"Depth limit {depth}: visited {' '.join(order):<24} -> {res}")
        if res == 'found':
            return depth
        if res == 'failure':
            return None
    return None

print("DLS with limit 2, goal = 'J'")
order = []
print("Result:", dls('A', 'J', 2, order), "| visited:", ' '.join(order))
print("\nIDDFS, goal = 'J'")
d = iddfs('A', 'J')
print("Goal found at depth", d)

# ----- Visualise the tree, colouring nodes by depth -----
G = nx.DiGraph([(p, c) for p, cs in tree.items() for c in cs])
# simple layered layout: each leaf gets its own x-slot, parents sit above children
pos, next_x = {}, [0]
def layout(n, d=0):
    kids = tree[n]
    if not kids:
        pos[n] = (next_x[0], -d); next_x[0] += 1
    else:
        for k in kids: layout(k, d + 1)
        pos[n] = (sum(pos[k][0] for k in kids) / len(kids), -d)
layout('A')
NAVY = '#0E367B'                       # Iqra University blue
colors = ['white' if n != 'J' else NAVY for n in G.nodes]
plt.figure(figsize=(6, 3.6))
nx.draw(G, pos, with_labels=False, node_color=colors, node_size=700,
        edgecolors=NAVY, edge_color=NAVY,
        arrows=False)
nx.draw_networkx_labels(G, pos, font_weight='bold',
        font_color={n: 'white' if n == 'J' else NAVY for n in G.nodes})
plt.title("Search tree (goal J highlighted)")
plt.savefig('lab04_tree.png', dpi=130, bbox_inches='tight')
print("Tree saved to lab04_tree.png")
