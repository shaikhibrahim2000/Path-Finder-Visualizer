# Importing required modules
from pyMaze import maze, agent, COLOR, textLabel  # For maze generation and visualization
from queue import PriorityQueue  # For implementing the open list in A*

def h(cell1, cell2):
    """
    Calculate the Manhattan distance heuristic between two cells.

    Parameters:
        cell1 (tuple): Coordinates (row, col) of the first cell.
        cell2 (tuple): Coordinates (row, col) of the second cell.

    Returns:
        int: Manhattan distance between the two cells.
    """
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def aStar(m, start=None):
    """
    Perform the A* search algorithm on the maze to find a path from start to goal.

    Parameters:
        m (maze): The maze object.
        start (tuple): Starting cell coordinates (row, col). Defaults to the bottom-right cell of the maze.

    Returns:
        tuple:
            searchPath (list): Sequence of cells explored during the search.
            aPath (dict): A dictionary mapping each visited cell to its predecessor.
            fwdPath (dict): A dictionary mapping the shortest path from the start cell to the goal cell.
    """
    # Default start cell to bottom-right corner if not provided
    if start is None:
        start = (m.rows, m.cols)

    # Priority queue for open nodes
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))  # (f_score, heuristic, cell)

    # Path and cost tracking
    aPath = {}
    g_score = {start: 0}  # Cost from start to the current cell
    f_score = {start: h(start, m._goal)}  # Estimated total cost through the current cell

    # List to track explored cells
    searchPath = [start]

    while not open.empty():
        # Get the cell with the lowest f-score
        currCell = open.get()[2]
        searchPath.append(currCell)

        # Check if the goal has been reached
        if currCell == m._goal:
            break

        # Explore neighbors of the current cell
        for d in 'ESNW':  # Directions: East, South, North, West
            if m.maze_map[currCell][d]:  # Check if movement in direction `d` is possible
                # Determine the child cell based on the direction
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                # Calculate tentative g and f scores for the child cell
                temp_g_score = g_score.get(currCell, float('inf')) + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)

                # Update if a better path is found
                if temp_f_score < f_score.get(childCell, float('inf')):
                    aPath[childCell] = currCell  # Map child cell to its parent
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))

    # Reconstruct the shortest path from goal to start
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    return searchPath, aPath, fwdPath

if __name__ == '__main__':
    """
    Main block to execute the A* algorithm on a generated maze and visualize the results.
    """
    # Create a maze of size 10x10
    m = maze(10, 10)  # Adjust dimensions as needed
    m.CreateMaze(2, 4)  # Set (2,4) as the goal cell, adjust for other valid cells

    # Perform A* search starting from (10,10)
    searchPath, aPath, fwdPath = aStar(m, (10, 10))  # Adjust start cell as required

    # Create agents to visualize the search path and A* path
    a = agent(m, 10, 10, goal=(2, 4), footprints=True, color=COLOR.blue)
    b = agent(m, 2, 4, goal=(10, 10), footprints=True, color=COLOR.red)

    # Visualize the paths
    m.tracePath({a: searchPath}, showMarked=True)  # Show the order of exploration
    m.tracePath({b: aPath})  # Show the A* path

    # Add labels for path lengths
    textLabel(m, 'A* Path Length', len(fwdPath) + 1)
    textLabel(m, 'A* Search Length', len(searchPath))

    # Run the maze visualization
    m.run()
