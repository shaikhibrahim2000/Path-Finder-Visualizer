# Importing necessary modules
from bfs import BFS  # Importing Breadth-First Search algorithm
from dfs import DFS  # Importing Depth-First Search algorithm
from pyMaze import maze, agent, COLOR, textLabel  # Importing pyMaze for maze creation and visualization
from timeit import timeit  # Importing timeit to measure execution time

# Create a maze object with dimensions 20x30
m = maze(20, 30)

# Generate a fully connected maze starting at position (1, 30) with 100% loop percentage
m.CreateMaze(1, 30, loopPercent=100)

# Perform Depth-First Search (DFS) on the maze
searchPath, dfsPath, fwdDFSPath = DFS(m)

# Perform Breadth-First Search (BFS) on the maze
bSearch, bfsPath, fwdBFSPath = BFS(m)

# Add text labels to display path lengths and search path lengths
textLabel(m, 'DFS Path Length', len(fwdDFSPath) + 1)  # Display the length of the DFS path
textLabel(m, 'BFS Path Length', len(fwdBFSPath) + 1)  # Display the length of the BFS path
textLabel(m, 'DFS Search Length', len(searchPath) + 1)  # Display the search area of DFS
textLabel(m, 'BFS Search Length', len(bSearch) + 1)  # Display the search area of BFS

# Create agents for visualization of paths
a = agent(m, footprints=True, color=COLOR.cyan)  # Agent for BFS path
b = agent(m, footprints=True, color=COLOR.yellow)  # Agent for DFS path

# Trace paths on the maze
m.tracePath({a: fwdBFSPath}, delay=100)  # Trace BFS path with a delay
m.tracePath({b: fwdDFSPath}, delay=100)  # Trace DFS path with a delay

# Measure and display the execution time for DFS and BFS algorithms
t1 = timeit(stmt='DFS(m)', number=1000, globals=globals())  # Time taken for 1000 runs of DFS
t2 = timeit(stmt='BFS(m)', number=1000, globals=globals())  # Time taken for 1000 runs of BFS

textLabel(m, 'DFS Time', t1)  # Display execution time for DFS
textLabel(m, 'BFS Time', t2)  # Display execution time for BFS

# Run the maze visualization
m.run()
