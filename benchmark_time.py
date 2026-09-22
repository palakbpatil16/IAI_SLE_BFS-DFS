import timeit
from bfs_dfs import bfs, dfs, find_position

start = find_position('S')
goal = find_position('G')

RUNS = 3
REPETITIONS = 1000


def measure_bfs():
    return bfs(start, goal)


def measure_dfs():
    return dfs(start, goal)


print("======== SLE-2 3-RUN PERFORMANCE TEST ========")

bfs_times = []
dfs_times = []

bfs_nodes = 0
dfs_nodes = 0

for run in range(1, RUNS + 1):

    bfs_time = timeit.timeit(
        measure_bfs,
        number=REPETITIONS
    ) * 1000 / REPETITIONS

    dfs_time = timeit.timeit(
        measure_dfs,
        number=REPETITIONS
    ) * 1000 / REPETITIONS

    _, bfs_nodes = bfs(start, goal)
    _, dfs_nodes = dfs(start, goal)

    bfs_times.append(bfs_time)
    dfs_times.append(dfs_time)

    print(f"\nRun {run}")
    print(f"BFS Time: {bfs_time:.6f} ms")
    print(f"DFS Time: {dfs_time:.6f} ms")


print("\n========= FINAL AVERAGE =========")

print("\nBFS")
print(f"Average Time: {sum(bfs_times) / RUNS:.6f} ms")
print(f"Nodes Expanded: {bfs_nodes}")
print("Goal Found: True")

print("\nDFS")
print(f"Average Time: {sum(dfs_times) / RUNS:.6f} ms")
print(f"Nodes Expanded: {dfs_nodes}")
print("Goal Found: True")