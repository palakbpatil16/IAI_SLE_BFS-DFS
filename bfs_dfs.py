from collections import deque

# -------------------------------------------------
# Maze
# S = Start
# G = Goal
# . = Open cell
# # = Wall
# -------------------------------------------------

maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'G']
]

ROWS = len(maze)
COLS = len(maze[0])


def find_position(symbol):
    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c] == symbol:
                return (r, c)
    return None


def get_neighbors(row, col):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if maze[nr][nc] != '#':
                neighbors.append((nr, nc))

    return neighbors


def bfs(start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in get_neighbors(*current):
            if neighbor not in visited:
                queue.append(neighbor)

    return False, nodes_expanded


def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in reversed(get_neighbors(*current)):
            if neighbor not in visited:
                stack.append(neighbor)

    return False, nodes_expanded


if __name__ == "__main__":
    start = find_position('S')
    goal = find_position('G')

    bfs_found, bfs_nodes = bfs(start, goal)
    dfs_found, dfs_nodes = dfs(start, goal)

    print("======== BFS Results ========")
    print("Goal found:", bfs_found)
    print("Nodes expanded:", bfs_nodes)

    print("\n======== DFS Results ========")
    print("Goal found:", dfs_found)
    print("Nodes expanded:", dfs_nodes)