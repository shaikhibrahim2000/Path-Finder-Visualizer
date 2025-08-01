# Importing necessary modules
from bfs import BFS  # Importing Breadth-First Search algorithm
from astar import aStar  # Importing A-Star algorithm
from pyMaze import maze, agent, COLOR, textLabel  # Importing pyMaze for maze creation and visualization
from timeit import timeit  # Importing timeit to measure execution time

# Create a maze object with dimensions 50x70
myMaze = maze(50, 70)

# Generate a fully connected maze (100% loop percentage)
myMaze.CreateMaze(loopPercent=100)

# Perform A-Star algorithm search on the maze
searchPath, aPath, fwdPath = aStar(myMaze)

# Perform Breadth-First Search algorithm on the maze
bSearch, bfsPath, fwdBFSPath = BFS(myMaze)

# Add text labels to display path lengths and search path lengths
l = textLabel(myMaze, 'A-Star Path Length', len(fwdPath) + 1)  # Display the length of the A-Star path
l = textLabel(myMaze, 'BFS Path Length', len(fwdBFSPath) + 1)  # Display the length of the BFS path
l = textLabel(myMaze, 'A-Star Search Length', len(searchPath) + 1)  # Display the search area of A-Star
l = textLabel(myMaze, 'BFS Search Length', len(bSearch) + 1)  # Display the search area of BFS

# Create agents for visualization of paths
a = agent(myMaze, footprints=True, color=COLOR.cyan, filled=True)  # Agent for BFS path
b = agent(myMaze, footprints=True, color=COLOR.yellow)  # Agent for A-Star path

# Trace paths on the maze
myMaze.tracePath({a: fwdBFSPath}, delay=50)  # Trace BFS path with a delay
myMaze.tracePath({b: fwdPath}, delay=50)  # Trace A-Star path with a delay

# Measure and display the execution time for A-Star and BFS algorithms
t1 = timeit(stmt='aStar(myMaze)', number=10, globals=globals())  # Time taken for 10 runs of A-Star
t2 = timeit(stmt='BFS(myMaze)', number=10, globals=globals())  # Time taken for 10 runs of BFS

textLabel(myMaze, 'A-Star Time', t1)  # Display execution time for A-Star
textLabel(myMaze, 'BFS Time', t2)  # Display execution time for BFS

# Run the maze visualization
myMaze.run()
