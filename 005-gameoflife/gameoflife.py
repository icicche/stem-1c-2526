# 005/01
# John Conway's Game of Life

# Functions definitions

def index(x, y):
    # Convert the coordinates (x, y) into a list index
    # with the 'snake' effect  |   ---->|   |->   ---|
    return (y % ROWS) * COLS + (x % COLS)


def near_alive(x, y):
    # Count how many neighbors of the cell (x, y) are
    # alive
    tot = 0

    tot += grid[index(x+1, y+1)] == A
    tot += grid[index(x+1, y-1)] == A
    tot += grid[index(x-1, y+1)] == A
    tot += grid[index(x-1, y-1)] == A
    tot += grid[index(x, y+1)] == A
    tot += grid[index(x, y-1)] == A
    tot += grid[index(x+1, y)] == A
    tot += grid[index(x-1, y)] == A

    return tot

def next_grid():
    # Make a copy of the grid where the state of each cell state
    # is updated according to the rules of Game of Life

    new_grid = []

    for y in range(ROWS):
        for x in range(COLS):

            # If (x, y) is alive and has less than 2 or
            # more than 3 alive neighbors, then it dies
            if (
                grid[index(x, y)] == A
                and (near_alive(x, y) < 2 or near_alive(x, y) > 3)
                ):
                    new_grid.append(D)

            # If (x, y) is dead and has exactly e alive
            # neighbors, then it becomes alive
            elif grid[index(x, y)] == D and near_alive(x, y) == 3:
                    new_grid.append(A)
            
            # Otherwise, the state of the cell stays the same
            else:
                 new_grid.append(grid[index(x, y)])
    
    return new_grid


# Initialize grid

ROWS = 4        # Grid rows
COLS = 5        # Grid columns

A = 'X'         # Displayed char for alive cells
D = 'O'         # Displayed char for dead cells

grid = [
    A, D, D, D, D,
    D, A, A, D, D,
    D, A, D, D, A,
    A, A, A, D, D
    ]

# Do some test for now

x = 3
y = 3

print(grid[index(x, y)])
grid = next_grid()
print(grid[index(x, y)])

