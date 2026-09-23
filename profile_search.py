from bfs_dfs import bfs, dfs

start = (0, 0)
goal = (4, 6)

print("======== BFS Results ========")

for _ in range(10000):
    bfs(start, goal)

print("BFS profiling completed.")

print("\n======== DFS Results ========")

for _ in range(10000):
    dfs(start, goal)

print("DFS profiling completed.")

print("\nProfiling program finished.")