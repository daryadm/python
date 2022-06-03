# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

"""

Conway's Game of Life

 - Zero-player game
 - N x M grid of lights
 - Starting position: some lights are ON, the rest are OFF
 - Each "turn" lights change according to these 4 rules:
 
 1. Any ON light with exactly 2 or 3 ON neighbours STAYS ON.
 2. All other ON lights TURN OFF. 
 3. Any OFF light with exactly 3 ON neighbours TURNS ON.
 4. All other OFF lights STAY OFF.
 
 
TODO:
 - Decide how to represent your state
 - Implement `next_state` 


ON  ON  OFF
OFF ON  OFF
OFF OFF OFF



"""


def next_state(state):
    """
        Given a state of the grid, return a new state object
        reflecting the input state updated by one "turn".
        I.e. immutably apply the 4 rules above one time.
    """
    new_state = []
    for cell in state:
        ns = get_neighbors(cell)
        for c in ns:
            new_state[c[0]][c[1]] =

    return new_state


starting_state = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 0, 0],
                  [1, 1, 1], [1, 2, 0], [2, 0, 1], [2, 1, 1], [2, 2, 0]]


def get_neighbors(cell):
    neighbors = []
    # find ns

    return 0


def stays_on(neighbors, cell_state):
    # count Ons
    # if cell_state is true and cntONs in (2,3) return true
    # if cell_state is false and cntOns == 3 return true


print("START:")
print(starting_state)

print("\nNext State:")
print(next_state(starting_state))
