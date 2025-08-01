# Importing required modules
from pyMaze import maze, agent, textLabel, COLOR  # Import maze generation and visualization
from collections import deque  # For an efficient queue implementation

def BFS(m, start=None):
    """
    Perform Breadth-First Search (BFS) on the maze to find a path from the start cell to the goal cell.

    Parameters:
        m (maze): The maze object.
        start (tuple): Starting cell coordinates (row, col). Defaults to the bottom-right cell of the maze.

    Returns:
        tuple:
            bSearch (list): Order of cells explored during the search.
            bfsPath (dict): A dictionary mapping each visited cell to its predecessor.
            fwdPath (dict): A dictionary mapping the shortest path from the start cell to the goal cell.
    """
    # Default start cell to bottom-right corner if not provided
    if start is None:
        start = (m.rows, m.cols)

    # Initialize BFS variables
    frontier = deque([start])  # Queue to manage cells to explore
    bfsPath = {start: start}  # Maps each cell to its parent
    explored = [start]  # Tracks all visited cells
    bSearch = [start]  # Sequence of cells explored during BFS

    while len(frontier) > 0:
        currCell = frontier.popleft()  # Dequeue the next cell to explore

        # If the goal cell is reached, stop searching
        if currCell == m._goal:
            break

        # Explore all possible directions from the current cell
        for d in 'ESNW':  # Directions: East, South, North, West
            if m.maze_map[currCell][d]:  # Check if movement in direction `d` is possible
                # Determine the child cell based on direction
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])

                # Skip cells that have already been visited
                if childCell in explored:
                    continue

                # Add the child cell to the frontier and explored lists
                frontier.append(childCell)
                explored.append(childCell)

                # Map the child cell to its parent in bfsPath
                bfsPath[childCell] = currCell
                bSearch.append(childCell)  # Record the exploration order

    # Trace the forward path from the goal cell to the start cell
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]

    return bSearch, bfsPath, fwdPath

if __name__ == '__main__':
    """
    Main block to execute BFS on a generated maze and visualize the results.
    """
    # Create a maze of size 10x10
    m = maze(10, 10)  # Adjust dimensions as needed
    m.CreateMaze(2, 4)  # Set (2,4) as the goal cell, adjust to other valid cells

    # Perform BFS starting from (10,10)
    bSearch, bfsPath, fwdPath = BFS(m, (10, 10))  # Adjust start cell as required

    # Create agents to visualize the search path and BFS path
    a = agent(m, 10, 10, goal=(2, 4), footprints=True, shape='square', color=COLOR.green)
    b = agent(m, 2, 4, goal=(10, 10), footprints=True, color=COLOR.red)

    # Visualize the paths
    m.tracePath({a: bSearch}, showMarked=True)  # Show the order of exploration
    m.tracePath({b: bfsPath})  # Show the BFS path

    # Run the maze visualization
    m.run()
