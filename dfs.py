# Importing necessary modules
from pyMaze import maze, agent, textLabel, COLOR  # Importing pyMaze for maze generation, visualization, and agent representation

def DFS(m, start=None):
    """
    Perform Depth First Search (DFS) on the maze to find a path from the start cell to the goal cell.
    
    Parameters:
        m (maze): The maze object.
        start (tuple): Starting cell coordinates (row, col). Defaults to the bottom-right cell of the maze.
    
    Returns:
        tuple: 
            dSearch (list): Order of cells explored during the search.
            dfsPath (dict): A dictionary mapping each visited cell to its predecessor.
            fwdPath (dict): A dictionary mapping the shortest path from the start cell to the goal cell.
    """
    # If no start cell is provided, default to the bottom-right cell
    if start is None:
        start = (m.rows, m.cols)

    # Initialize the explored and frontier lists
    explored = [start]  # Tracks all visited cells
    frontier = [start]  # Tracks the current stack of cells for DFS
    dfsPath = {}  # Maps each cell to its predecessor
    dSearch = []  # Order of cells visited during the search

    while len(frontier) > 0:
        currCell = frontier.pop()  # Remove and process the last cell in the stack
        dSearch.append(currCell)  # Add the current cell to the search order
        if currCell == m._goal:  # Check if the goal cell is reached
            break

        # Explore all possible directions from the current cell
        poss = 0  # Tracks the number of valid child cells
        for d in 'ESNW':  # Directions: East, South, North, West
            if m.maze_map[currCell][d] == True:  # Check if movement in direction `d` is possible
                # Determine the child cell based on direction
                if d == 'E':
                    child = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    child = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    child = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    child = (currCell[0] + 1, currCell[1])

                if child in explored:  # Skip already visited cells
                    continue

                poss += 1  # Increment valid child count
                explored.append(child)  # Mark the child as explored
                frontier.append(child)  # Add the child to the stack
                dfsPath[child] = currCell  # Record the path from parent to child

        if poss > 1:  # Mark cells with multiple children for visualization
            m.markCells.append(currCell)

    # Trace the forward path from the goal to the start cell
    fwdPath = {}  # Maps each cell in the forward path to its successor
    cell = m._goal
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]

    return dSearch, dfsPath, fwdPath

if __name__ == '__main__':
    """
    Main block to execute the DFS algorithm on a generated maze and visualize the result.
    """
    # Create a maze of size 10x10
    m = maze(10, 10)  # Adjust dimensions as needed
    m.CreateMaze(2, 4)  # Set (2,4) as the goal cell, adjust to any other valid cell

    # Perform DFS on the maze starting from (10,10)
    dSearch, dfsPath, fwdPath = DFS(m, (10, 10))  # Change start and goal cells as required

    # Create agents to visualize the search path and DFS path
    a = agent(m, 10, 10, goal=(2, 4), footprints=True, shape='square', color=COLOR.green)
    b = agent(m, 2, 4, goal=(10, 10), footprints=True, color=COLOR.red)

    # Visualize the paths
    m.tracePath({a: dSearch}, showMarked=True)  # Show the order of exploration
    m.tracePath({b: dfsPath})  # Show the DFS path

    # Run the maze visualization
    m.run()
