from pyMaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue
import math

def h(cell1, cell2, p=2):
    """
    Minkowski distance heuristic
    p=1: Manhattan distance
    p=2: Euclidean distance
    p→∞: Chebyshev distance
    """
    x1, y1 = cell1
    x2, y2 = cell2
    return ((abs(x1 - x2)**p) + (abs(y1 - y2)**p))**(1/p)

def aStar(m, start=None, p=2):
    if start is None:
        start = (m.rows, m.cols)
    
    # Priority queue for open nodes
    open = PriorityQueue()
    open.put((h(start, m._goal, p), h(start, m._goal, p), start))
    
    # Path tracking
    aPath = {}
    
    # Cost tracking
    g_score = {start: 0}
    f_score = {start: h(start, m._goal, p)}
    
    # Explored cells
    searchPath = [start]
    
    while not open.empty():
        # Get the cell with lowest f-score
        currCell = open.get()[2]
        searchPath.append(currCell)
        
        # Goal check
        if currCell == m._goal:
            break
        
        # Explore neighbors
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                # Determine child cell based on direction
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                
                # Calculate tentative scores
                temp_g_score = g_score.get(currCell, float('inf')) + 1
                temp_f_score = temp_g_score + h(childCell, m._goal, p)
                
                # Update if better path found
                if (temp_f_score < f_score.get(childCell, float('inf'))):
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((f_score[childCell], h(childCell, m._goal, p), childCell))
    
    # Reconstruct forward path
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    
    return searchPath, aPath, fwdPath

if __name__ == '__main__':
    # Create a 10x10 maze
    m = maze(10, 10)
    m.CreateMaze(2, 4)  # Goal at (2,4)

    # Different Minkowski distance parameters
    distance_types = [
        (1, "Manhattan (p=1)"),
        (2, "Euclidean (p=2)"),
        (3, "Minkowski (p=3)"),
        (4, "Minkowski (p=4)")
    ]

    for p, name in distance_types:
        # Run A* from (10,10)
        searchPath, aPath, fwdPath = aStar(m, (10, 10), p)

        # Create agents for visualization
        a = agent(m, 10, 10, goal=(2,4), footprints=True, color=COLOR.blue)
        b = agent(m, 2, 4, goal=(10,10), footprints=True, color=COLOR.red)

        # Trace paths
        m.tracePath({a:searchPath}, showMarked=True)
        m.tracePath({b:aPath})

        # Add path length labels
        textLabel(m, f'{name} Path Length', len(fwdPath)+1)
        textLabel(m, f'{name} Search Length', len(searchPath))

        m.run()