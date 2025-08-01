# Importing necessary modules
from astar import aStar  # Importing the A-Star algorithm with Manhattan heuristic
from astar2 import aStar2  # Importing the A-Star algorithm with Euclidean heuristic
from pyMaze import maze, agent, COLOR, textLabel  # Importing pyMaze for maze creation and visualization
from timeit import timeit  # Importing timeit for performance measurement

# Initialize counters for comparison results
f1, f2, f3 = 0, 0, 0  # Counters for final path length comparison
s1, s2, s3 = 0, 0, 0  # Counters for search path length comparison

# Loop to test and compare algorithms over 100 iterations
for _ in range(100):
    # Create a new maze object with dimensions 20x30 and 100% loop connectivity
    myMaze = maze(20, 30)
    myMaze.CreateMaze(loopPercent=100)

    # Run A-Star algorithm with Manhattan heuristic
    searchPath, aPath, fwdPath = aStar(myMaze)
    
    # Run A-Star algorithm with Euclidean heuristic
    searchPath2, aPath2, fwdPath2 = aStar2(myMaze)

    # Compare the final path lengths
    if len(fwdPath) == len(fwdPath2):  # If both algorithms produce paths of the same length
        f1 += 1
    elif len(fwdPath) < len(fwdPath2):  # If Manhattan heuristic produces a shorter final path
        f2 += 1
    else:  # If Euclidean heuristic produces a shorter final path
        f3 += 1

    # Compare the search path lengths
    if len(searchPath) == len(searchPath2):  # If both algorithms search the same number of nodes
        s1 += 1
    elif len(searchPath) < len(searchPath2):  # If Manhattan heuristic explores fewer nodes
        s2 += 1
    else:  # If Euclidean heuristic explores fewer nodes
        s3 += 1

# Print the results of the final path comparison
print('Final Path Comparison Result') 
print(f'Both have same Final Path length for {f1} times.')  # Equal final path lengths
print(f'Manhattan has lesser Final Path length for {f2} times.')  # Manhattan shorter
print(f'Euclidean has lesser Final Path length for {f3} times.')  # Euclidean shorter

print('--------------------------------------------')

# Print the results of the search path comparison
print('Search Path Comparison Result')
print(f'Both have same Search Path length for {s1} times.')  # Equal search path lengths
print(f'Manhattan has lesser Search Path length for {s2} times.')  # Manhattan searches less
print(f'Euclidean has lesser Search Path length for {s3} times.')  # Euclidean searches less
