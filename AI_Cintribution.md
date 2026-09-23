# AI Contribution Log
## SLE-2: BFS vs DFS Maze Performance Profiling

**Name:** Palak  Patil
**PRN:** 25UAM093 
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Project:** BFS vs DFS Maze Performance Profiling  

---

## 1. AI Tools Used

The following AI tools were used during the development of this SLE-2 project:

- ChatGPT
- GitHub Copilot

---

## 2. Contribution Log

| Sr. No. | AI Tool | Purpose / Assistance | Student's Work |
|---|---|---|---|
| 1 | ChatGPT | Helped understand the SLE-2 profiling requirements and report structure. | Understood the requirements and prepared the experiment. |
| 2 | ChatGPT | Explained BFS and DFS concepts and their implementation. | Implemented and tested BFS and DFS. |
| 3 | GitHub Copilot | Provided code suggestions for maze search and performance-testing code. | Reviewed, modified, and tested the suggested code. |
| 4 | ChatGPT | Helped understand Python `timeit` and execution-time measurement. | Ran the benchmark programs and collected actual timing results. |
| 5 | ChatGPT | Helped understand manual node counting. | Added and verified the node counter. |
| 6 | ChatGPT | Helped understand Best, Average, and Worst Case testing. | Selected goal positions `(0,1)`, `(2,4)`, and `(4,6)` and performed the experiments. |
| 7 | ChatGPT | Helped understand and troubleshoot py-spy profiling. | Installed and executed py-spy and generated `profile.svg`. |
| 8 | ChatGPT | Helped troubleshoot Git/GitHub commands and repository organization. | Managed the repository, commits, and GitHub push operations. |
| 9 | ChatGPT | Helped organize the README and project documentation. | Reviewed the documentation and added the actual project information and results. |

---

## 3. AI-Assisted Code

AI assistance was used for understanding and generating code suggestions related to:

- BFS implementation
- DFS implementation
- Maze representation
- Execution-time benchmarking
- Node counting
- Best Case testing
- Average Case testing
- Worst Case testing
- `timeit` usage
- py-spy profiling setup
- Git/GitHub troubleshooting
- Project documentation

The AI-generated suggestions were reviewed and modified according to the requirements of the experiment.

---

## 4. Work Performed by Student

The following work was performed and verified by the student:

- Created and used the maze problem.
- Defined the start position `(0,0)`.
- Selected Best Case goal `(0,1)`.
- Selected Average Case goal `(2,4)`.
- Selected Worst Case goal `(4,6)`.
- Implemented and tested BFS.
- Implemented and tested DFS.
- Ran the programs locally.
- Performed the timing experiments.
- Performed three experimental runs.
- Collected the actual execution-time results.
- Verified the number of nodes expanded.
- Installed and executed py-spy.
- Generated the profiling output.
- Organized the project files.
- Created and maintained the GitHub repository.
- Prepared the final experimental analysis.

---

## 5. Actual Experimental Results

The reported values were obtained from actual program execution.

### Case Analysis

| Case | Goal Position | BFS Time (ms) | BFS Nodes | DFS Time (ms) | DFS Nodes |
|---|---|---:|---:|---:|---:|
| Best Case | `(0,1)` | 0.005126 | 2 | 0.005481 | 2 |
| Average Case | `(2,4)` | 0.032979 | 9 | 0.060422 | 15 |
| Worst Case | `(4,6)` | 0.071114 | 22 | 0.071297 | 23 |

### Goal Status

| Case | BFS | DFS |
|---|---|---|
| Best Case | True | True |
| Average Case | True | True |
| Worst Case | True | True |

---

## 6. Ownership Statement

AI tools were used as assistance for learning, code suggestions, troubleshooting, and documentation.

The student reviewed and understood the suggestions, executed the programs locally, collected the experimental data, verified the results, and performed the final analysis.

The performance values reported in this project were obtained from the student's actual experimental runs.
