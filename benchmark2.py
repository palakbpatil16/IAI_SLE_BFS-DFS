import timeit
from bfs_dfs import bfs, dfs, get_neighbors

START = (0, 0)

# Three goal positions in the same maze
CASES = {
    "Best Case": (0, 1),
    "Average Case": (2, 4),
    "Worst Case": (4, 6)
}

RUNS = 3
REPETITIONS = 1000


def measure_bfs(goal):
    return bfs(START, goal)


def measure_dfs(goal):
    return dfs(START, goal)


print("==============================================")
print(" SLE-2: BFS vs DFS MAZE CASE ANALYSIS")
print("==============================================")
print("Start Position: (0, 0)")
print(f"Runs: {RUNS}")
print(f"Repetitions per run: {REPETITIONS}")


for case_name, goal in CASES.items():

    print("\n----------------------------------------------")
    print(case_name)
    print("----------------------------------------------")
    print("Goal Position:", goal)

    bfs_times = []
    dfs_times = []

    bfs_nodes = 0
    dfs_nodes = 0

    for _ in range(RUNS):

        bfs_time = timeit.timeit(
            lambda: measure_bfs(goal),
            number=REPETITIONS
        ) * 1000 / REPETITIONS

        dfs_time = timeit.timeit(
            lambda: measure_dfs(goal),
            number=REPETITIONS
        ) * 1000 / REPETITIONS

        bfs_times.append(bfs_time)
        dfs_times.append(dfs_time)

        _, bfs_nodes = bfs(START, goal)
        _, dfs_nodes = dfs(START, goal)

    bfs_average = sum(bfs_times) / RUNS
    dfs_average = sum(dfs_times) / RUNS

    bfs_found, _ = bfs(START, goal)
    dfs_found, _ = dfs(START, goal)

    print("\nBFS:")
    print(f"Average Time: {bfs_average:.6f} ms")
    print(f"Nodes Expanded: {bfs_nodes}")
    print(f"Goal Found: {bfs_found}")

    print("\nDFS:")
    print(f"Average Time: {dfs_average:.6f} ms")
    print(f"Nodes Expanded: {dfs_nodes}")
    print(f"Goal Found: {dfs_found}")


print("\n==============================================")
print(" Comparison completed successfully")
print("==============================================")