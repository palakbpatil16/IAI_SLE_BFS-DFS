# SLE-2: BFS vs DFS Maze Performance Profiling

**Name:** Palak  
**PRN:** 25UAM092  
**Course:** Introduction to Artificial Intelligence  
**SLE:** SLE-2  

## 1. Problem Statement

The objective of this project is to compare the performance of **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** for solving a grid-based maze.

Both algorithms start from the same starting position and search for a specified goal. Their performance is compared using:

- Execution time
- Number of nodes expanded
- Best, Average and Worst Case experiments
- Python profiling using `py-spy`

## 2. Maze

```text
S . . # . . .
# # . # . # .
. . . . . # .
. # # # . # .
. . . . . . G

S = Start
G = Goal
. = Open cell
# = Wall

Starting position: (0, 0)

3. Algorithms
BFS

BFS explores nodes level by level using a queue (FIFO).

DFS

DFS explores one branch deeply before backtracking using a stack (LIFO).

For an adjacency-list graph, both algorithms have:

Time Complexity: O(V + E)

where V is the number of vertices and E is the number of edges.

4. Experimental Cases

Three goal positions are used for testing:

Case	Goal
Best Case	(0, 1)
Average Case	(2, 4)
Worst Case	(4, 6)

The actual execution time and node counts are obtained from the Python programs.

5. Performance Measurement

Python's timeit module is used to measure execution time.

Three runs are performed for BFS and DFS, and their average execution time is calculated.

Case	BFS Time	BFS Nodes	DFS Time	DFS Nodes
Best	Actual result	Actual result	Actual result	Actual result
Average	Actual result	Actual result	Actual result	Actual result
Worst	Actual result	Actual result	Actual result	Actual result
6. Profiling

py-spy is used to profile the Python program and generate a flame graph.

The profiling output is:

profile.svg

The flame graph helps identify which functions consume execution time during BFS and DFS.

7. Project Files
SLE2_BFS_DFS_MAZE/
│
├── bfs_dfs.py
├── benchmark.py
├── benchmark2.py
├── profile_search.py
├── profile.svg
├── README.md
├── AI_CONTRIBUTION_LOG.md
└── .gitignore
8. How to Run
python bfs_dfs.py
python benchmark.py
python benchmark2.py
python profile_search.py

To generate the profiling graph:

py-spy record --output profile.svg -- python profile_search.py
9. Conclusion

This experiment compares BFS and DFS using the same maze and starting position. The algorithms are evaluated using execution time and nodes expanded for different goal positions.

The experiment also demonstrates practical use of Python benchmarking with timeit and performance profiling with py-spy.
